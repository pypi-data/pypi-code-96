import numpy as np
import pandas as pd

#
from metaDMG.fit import fit_utils

columns = [
    "tax_id",
    "direction",
    "position",
    *fit_utils.ref_obs_bases,
]


#%%

bases_forward = "CT"
bases_reverse = "GA"


def get_subsitution_bases_to_keep():
    forward = bases_forward
    reverse = bases_reverse
    bases_to_keep = [forward[0], forward, reverse[0], reverse]
    return bases_to_keep


def get_base_columns(df):
    base_columns = []
    for column in df.columns:
        if (
            len(column) == 2
            and column[0] in fit_utils.ACTG
            and column[1] in fit_utils.ACTG
        ):
            base_columns.append(column)
    return base_columns


def get_reference_columns(df, ref):
    ref_columns = []
    for column in get_base_columns(df):
        if column[0] == ref:
            ref_columns.append(column)
    return ref_columns


def add_reference_counts(df, ref):
    reference_columns = get_reference_columns(df, ref)
    df[ref] = df[reference_columns].sum(axis=1)
    return df


def compute_fraction_and_uncertainty(x, N, set_zero_to_nan=False):
    f = x / N
    if set_zero_to_nan:
        f = f.mask(x == 0, np.nan)
    sf = np.sqrt(f * (1 - f) / N)
    return f, sf


def compute_error_rates(df, ref, obs):
    s_ref_obs = ref + obs
    x = df[s_ref_obs]
    N_ref = df[ref]
    f, sf = compute_fraction_and_uncertainty(x, N_ref)
    return f, sf


def add_error_rates(df, ref, obs, include_uncertainties=False):
    f, sf = compute_error_rates(df, ref, obs)
    df[f"f_{ref}{obs}"] = f
    if include_uncertainties:
        df[f"sf_{ref}{obs}"] = sf
    return df


def make_position_1_indexed(df):
    "Make the position, z, one-indexed (opposed to zero-indexed)"
    df["position"] += 1
    return df


def make_reverse_position_negative(df):
    is_reverse = ~fit_utils.is_forward(df)
    df["position"] = (is_reverse * (-1) + (~is_reverse)) * df["position"]
    # pos = df["position"]
    # pos_reverse = pos[is_reverse]
    # pos_reverse *= -1
    # df["position"] = df["position"].mask(is_reverse, -pos_reverse)
    return df


# def sort_by_alignments(df_top_N):
#     pos = df_top_N["position"]
#     df_top_N["order"] = pos.mask(pos > 0, 1 / pos)
#     return df_top_N.sort_values(
#         by=["N_alignments", "tax_id", "order"], ascending=False
#     ).drop(columns=["order"])


# def replace_nans_with_zeroes(df):
# return df.fillna(0)


def compute_k_sum_total(group):
    k_sum_total = 0
    forward_bases = bases_forward[0] + bases_forward[1]
    k_sum_total += group[group.position > 0][forward_bases].sum()
    reverse_bases = bases_reverse[0] + bases_reverse[1]
    k_sum_total += group[group.position < 0][reverse_bases].sum()
    return k_sum_total


def add_k_sum_counts(df):
    ds = df.groupby("tax_id").apply(compute_k_sum_total)
    ds = ds.reset_index().rename(columns={0: "k_sum_total"})
    df = pd.merge(df, ds, on=["tax_id"])
    return df


def compute_min_N_in_group(group):
    min_N_forward = group[group.position > 0][bases_forward[0]].min()
    min_N_reverse = group[group.position < 0][bases_reverse[0]].min()
    return min(min_N_forward, min_N_reverse)


def add_min_N_in_group(df):
    ds = df.groupby("tax_id").apply(compute_min_N_in_group)
    ds = ds.reset_index().rename(columns={0: "min_N_in_group"})
    df = pd.merge(df, ds, on=["tax_id"])
    return df


# def filter_cut_based_on_cfg(df, cfg):
#     # query = f"(N_alignments >= {cfg.min_alignments}) "
#     query = f"(k_sum_total >= {cfg.min_k_sum})"
#     query += f"& (min_N_in_group >= {cfg.min_N_at_each_pos})"
#     return df.query(query)


def add_k_N_x_names(df):
    # mask_forward = df["direction"] == "5'"
    mask_forward = fit_utils.is_forward(df)
    df["k"] = np.where(mask_forward, df["CT"], df["GA"])
    df["N"] = np.where(mask_forward, df["C"], df["G"])
    df["f"] = df["k"] / df["N"]
    df["|x|"] = np.abs(df["position"])
    return df


def rename_columns(df):
    return df.rename(columns={"#taxid": "tax_id"})


def compute(config):

    df = (
        pd.read_csv(config["path_mismatches_txt"], sep="\t")
        .pipe(rename_columns)
        .pipe(add_reference_counts, ref=bases_forward[0])
        .pipe(add_reference_counts, ref=bases_reverse[0])
        .pipe(add_error_rates, ref=bases_forward[0], obs=bases_forward[1])
        .pipe(add_error_rates, ref=bases_reverse[0], obs=bases_reverse[1])
        .pipe(make_position_1_indexed)
        .pipe(make_reverse_position_negative)
        .pipe(add_k_N_x_names)
        .pipe(add_k_sum_counts)
        .pipe(add_min_N_in_group)
        # .pipe(filter_cut_based_on_cfg, cfg)
        .reset_index(drop=True)
        .fillna(0)
    )

    df["sample"] = config["sample"]
    categories = ["tax_id", "direction", "sample", "k_sum_total", "min_N_in_group"]
    df_mismatches = fit_utils.downcast_dataframe(df, categories, fully_automatic=False)

    return df_mismatches

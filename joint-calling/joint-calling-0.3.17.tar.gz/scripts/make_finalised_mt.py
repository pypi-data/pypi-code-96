#!/usr/bin/env python

"""
Generate final annotated, soft-filtered Matrix Table
"""

import logging
from typing import Optional

import click
import hail as hl

from joint_calling.utils import get_validation_callback, file_exists
from joint_calling import utils, _version

logger = logging.getLogger('joint-calling')
logger.setLevel('INFO')


@click.command()
@click.version_option(_version.__version__)
@click.option(
    '--mt',
    'mt_path',
    required=True,
    callback=get_validation_callback(ext='mt', must_exist=True),
    help='path to the raw sparse Matrix Table generated by combine_gvcfs.py',
)
@click.option(
    '--out-mt',
    'out_mt_path',
    required=True,
    callback=get_validation_callback(ext='mt', must_exist=False),
    help='path to write the final annotated soft-filtered Matrix Table',
)
@click.option(
    '--out-nonref-mt',
    'out_nonref_mt_path',
    callback=get_validation_callback(ext='mt', must_exist=False),
    help='write a version of output Matrix Table without reference blocks',
)
@click.option(
    '--meta-ht',
    'meta_ht_path',
    required=True,
    help='Table generated by sample_qc.py',
)
@click.option(
    '--final-filter-ht',
    'vqsr_final_filter_ht_path',
    required=True,
    help='Table with AS-VQSR annotations',
)
@click.option(
    '--local-tmp-dir',
    'local_tmp_dir',
    help='local directory for temporary files and Hail logs (must be local).',
)
@click.option(
    '--overwrite/--reuse',
    'overwrite',
    is_flag=True,
    help='if an intermediate or a final file exists, skip running the code '
    'that generates it.',
)
@click.option(
    '--hail-billing',
    'hail_billing',
    help='Hail billing account ID.',
)
def main(
    mt_path: str,
    out_mt_path: str,
    out_nonref_mt_path: Optional[str],
    meta_ht_path: str,
    vqsr_final_filter_ht_path: str,
    local_tmp_dir: str,
    overwrite: bool,  # pylint: disable=unused-argument
    hail_billing: str,  # pylint: disable=unused-argument
):  # pylint: disable=missing-function-docstring
    utils.init_hail('make_finalised_mt', local_tmp_dir)

    if file_exists(out_mt_path):
        if overwrite:
            logger.info(f'Output {out_mt_path} exists and will be overwritten')
        else:
            logger.error(
                f'Output file {out_mt_path} exists, use --overwrite to overwrite'
            )
            return

    # This will return a table with split multiallelics, and thus GT as a field
    mt = utils.get_mt(
        mt_path, split=True, add_meta=True, meta_ht=hl.read_table(meta_ht_path)
    )

    vqsr_ht = hl.read_table(vqsr_final_filter_ht_path)
    mt = mt.annotate_rows(**vqsr_ht[mt.row_key])
    mt = mt.annotate_globals(**vqsr_ht.index_globals())
    mt.write(out_mt_path, overwrite=True)

    if out_nonref_mt_path:
        mt = mt.filter_rows((hl.len(mt.alleles) > 1) & hl.agg.any(mt.GT.is_non_ref()))
        mt.write(out_nonref_mt_path, overwrite=True)


if __name__ == '__main__':
    main()  # pylint: disable=E1120

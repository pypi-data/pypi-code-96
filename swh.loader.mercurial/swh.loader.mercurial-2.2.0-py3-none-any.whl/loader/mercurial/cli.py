# Copyright (C) 2018-2021  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from itertools import chain
import logging

import click
from deprecated import deprecated

from swh.loader.mercurial.utils import parse_visit_date

LOGLEVELS = list(
    chain.from_iterable(
        (logging._levelToName[lvl], logging._levelToName[lvl].lower())
        for lvl in sorted(logging._levelToName.keys())
    )
)


@click.command()
@click.argument("origin-url")
@click.option(
    "--hg-directory",
    "-d",
    help=(
        "Path to the hg (local) directory to load from. "
        "If unset, the hg repo will be cloned from the "
        "given (origin) url."
    ),
)
@click.option("--hg-archive", "-a", help=("Path to the hg archive file to load from."))
@click.option("--visit-date", "-D", help="Visit date (defaults to now).")
@click.option("--log-level", "-l", type=click.Choice(LOGLEVELS), help="Log level.")
@deprecated(
    version="0.4.0", reason="Use `swh loader run mercurial|mercurial_from_disk` instead"
)
def main(
    origin_url, hg_directory=None, hg_archive=None, visit_date=None, log_level=None
):
    from swh.storage import get_storage

    logging.basicConfig(
        level=(log_level or "DEBUG").upper(),
        format="%(asctime)s %(process)d %(message)s",
    )

    visit_date = parse_visit_date(visit_date or "now")

    kwargs = {"visit_date": visit_date, "url": origin_url}
    if hg_archive:
        from .loader import HgArchiveBundle20Loader as HgLoader

        kwargs["archive_path"] = hg_archive
    else:
        from .loader import HgBundle20Loader as HgLoader

        kwargs["directory"] = hg_directory

    storage = get_storage(cls="memory")
    return HgLoader(storage, **kwargs).load()


if __name__ == "__main__":
    main()

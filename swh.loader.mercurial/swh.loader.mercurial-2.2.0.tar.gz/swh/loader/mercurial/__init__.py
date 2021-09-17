# Copyright (C) 2019  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information


from typing import Any, Mapping


def register() -> Mapping[str, Any]:
    """Register the current worker module's definition"""
    from .loader import HgBundle20Loader

    return {
        "task_modules": [f"{__name__}.tasks"],
        "loader": HgBundle20Loader,
    }


def register_from_disk() -> Mapping[str, Any]:
    """Register the current worker module's definition"""
    from .from_disk import HgLoaderFromDisk

    return {
        "task_modules": [f"{__name__}.tasks_from_disk"],
        "loader": HgLoaderFromDisk,
    }

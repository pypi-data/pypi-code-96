import logging
import os
import shutil
import sys
from typing import Dict, List

from tox.config.loader.memory import MemoryLoader
from tox.config.loader.section import Section
from tox.config.main import Config
from tox.config.sets import ConfigSet
from tox.config.types import EnvList
from tox.plugin import impl
from virtualenv.discovery.py_info import PythonInfo


def is_running_on_actions() -> bool:
    """:return: True if running on Github Actions platform"""
    # https://docs.github.com/en/actions/reference/environment-variables#default-environment-variables
    return os.environ.get("GITHUB_ACTIONS") == "true"


def get_python_version_keys() -> List[str]:
    """:return: python spec for the python interpreter"""
    python_exe = shutil.which("python") or sys.executable
    info = PythonInfo.from_exe(exe=python_exe)
    major_version = str(info.version_info[0])
    major_minor_version = ".".join([str(i) for i in info.version_info[:2]])
    if "PyPy" == info.implementation:
        return [f"pypy-{major_minor_version}", f"pypy-{major_version}", f"pypy{major_version}"]
    elif hasattr(sys, "pyston_version_info"):  # Pyston
        return [f"piston-{major_minor_version}", f"pyston-{major_version}"]
    else:  # Assume this is running on CPython
        return [major_minor_version, major_version]


class GhActionsConfigSet(ConfigSet):
    def register_config(self) -> None:
        self.add_config("python", of_type=Dict[str, EnvList], default={}, desc="python version to mapping")


@impl
def tox_add_core_config(core_conf: ConfigSet, config: "Config") -> None:  # noqa: U100
    bail_reason = None
    if not is_running_on_actions():
        bail_reason = "tox is not running in GitHub Actions"
    elif getattr(config.options.env, "use_default_list", False) is False:
        bail_reason = f"envlist is explicitly given via {'TOXENV'if os.environ.get('TOXENV') else '-e flag'}"
    if bail_reason:
        logging.warning("tox-gh won't override envlist because %s", bail_reason)
        return

    logging.warning("running tox-gh")
    gh_config = config.get_section_config(Section(None, "gh"), base=[], of_type=GhActionsConfigSet, for_env=None)
    python_mapping: Dict[str, EnvList] = gh_config["python"]

    env_list = next((python_mapping[i] for i in get_python_version_keys() if i in python_mapping), None)
    if env_list is not None:  # override the env_list core configuration with our values
        logging.warning("tox-gh set %s", ", ".join(env_list))
        config.core.loaders.insert(0, MemoryLoader(env_list=env_list))

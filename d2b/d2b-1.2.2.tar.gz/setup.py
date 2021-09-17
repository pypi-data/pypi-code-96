# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['d2b', 'd2b.commands', 'd2b.internal_plugins']

package_data = \
{'': ['*'], 'd2b.commands': ['scaffold_template/*']}

install_requires = \
['pluggy>=0.12,<1.0.0a1']

entry_points = \
{'console_scripts': ['d2b = d2b.cli:main']}

setup_kwargs = {
    'name': 'd2b',
    'version': '1.2.2',
    'description': 'Organize data in the BIDS format',
    'long_description': '# d2b\n\nOrganize data in the BIDS format.\n\n[![PyPI Version](https://img.shields.io/pypi/v/d2b.svg)](https://pypi.org/project/d2b/) [![codecov](https://codecov.io/gh/d2b-dev/d2b/branch/master/graph/badge.svg?token=B83CY7Z0NL)](https://codecov.io/gh/d2b-dev/d2b) [![Tests](https://github.com/d2b-dev/d2b/actions/workflows/test.yaml/badge.svg)](https://github.com/d2b-dev/d2b/actions/workflows/test.yaml) [![Code Style](https://github.com/d2b-dev/d2b/actions/workflows/lint.yaml/badge.svg)](https://github.com/d2b-dev/d2b/actions/workflows/lint.yaml) [![Type Check](https://github.com/d2b-dev/d2b/actions/workflows/type-check.yaml/badge.svg)](https://github.com/d2b-dev/d2b/actions/workflows/type-check.yaml)\n\nCompatible with `dcm2bids` config files.\n\n## Installation\n\n```bash\npip install d2b\n```\n\n## Usage\n\nThe singular CLI entrypoint:\n\n```bash\n$ d2b --help\nusage: d2b [-h] [-v] {run,scaffold} ...\n\nd2b - Organize data in the BIDS format\n\npositional arguments:\n  {run,scaffold}\n\noptional arguments:\n  -h, --help      show this help message and exit\n  -v, --version   show program\'s version number and exit\n```\n\nScaffold a BIDS dataset:\n\n```bash\n$ d2b scaffold --help\nusage: d2b scaffold [-h] out_dir\n\nScaffold a BIDS dataset directory structure\n\npositional arguments:\n  out_dir     Output BIDS directory\n\noptional arguments:\n  -h, --help  show this help message and exit\n```\n\nOrganize nifti data (sidecars required) into a BIDS-compliant structure:\n\n```bash\n$ d2b run --help\nusage: d2b run [-h] -c CONFIG_FILE -p PARTICIPANT -o OUT_DIR [-s SESSION] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] in_dir [in_dir ...]\n\nOrganize data in the BIDS format\n\npositional arguments:\n  in_dir                Directory(ies) containing files to organize\n\nrequired arguments:\n  -c CONFIG_FILE, --config CONFIG_FILE\n                        JSON configuration file (see example/config.json)\n  -p PARTICIPANT, --participant PARTICIPANT\n                        Participant ID\n  -o OUT_DIR, --out-dir OUT_DIR\n                        Output BIDS directory\n\noptional arguments:\n  -s SESSION, --session SESSION\n                        Session ID\n  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}\n                        Set logging level\n```\n\n## Motivation\n\nThis package offers a pluggable BIDS-ification workflow which attempts to mirror parts of the [`dcm2bids`](https://github.com/UNFmontreal/Dcm2Bids) CLI.\n\n**This most important goal of this package is to support existing `dcm2bids` config files.**\n\nA notable difference between `d2b` and `dcm2bids` is that the default assumption made by `d2b` is that you\'re **_NOT_** giving it DICOM data as input (although, if this is your use-case, there\'s a plugin to enable going straight from DICOM -> BIDS).\n\nOut of the box, `d2b` assumes that you\'re working with NIfTI + NIfTI sidecar data.\n\nThe general premise of the `dcm2bids` workflow is very nice: _describe the files your interested in (in config) and the software will take the descriptions, find matching files, and organize those files accordingly_.\n\n`d2b` (together with plugins powered by [`pluggy`](https://github.com/pytest-dev/pluggy)) tries to offer all functionality that `dcm2bids` offers, with an aim toward being _extensible_.\n\nWe wanted `dcm2bids` to do things that it was [never intended to do](https://github.com/UNFmontreal/Dcm2Bids/issues/100#issuecomment-733033859), hence `d2b` was born.\n\n## `d2b` and `dcm2bids`\n\nSimilarities:\n\n- **Config files used with `dcm2bids` are compatible with `d2b`**\n- The `d2b run` command corresponds to `dcm2bids`\n- The `d2b scaffold` command corresponds to `dcm2bids_scaffold`\n\nDifferences:\n\n- `d2b` has a plugin system so that users can extend the core functionality to fit the needs of their specific use-case.\n- The `d2b` code architecture is meant to make the BIDS dataset generation process less error prone.\n- Out of the box, `d2b` doesn\'t try to convert DICOM files and in fact `dcm2niix` doesn\'t even need to be installed. To do DICOM -> BIDS conversions install the [`d2b-dcm2niix`](https://github.com/d2b-dev/d2b-dcm2niix) plugin\n- Out of the box `defaceTpl` is no longer supported.\n\n<!-- ## Config File Schema -->\n\n## Writing config files\n\nTo make writing `d2b` config files easier, we\'ve included a [JSON schema](https://json-schema.org/) specification file ([schema.json](https://github.com/d2b-dev/d2b/blob/master/json-schemas/schema.json)). You can use this file in editors that support JSON Schema definitions to provide autocompletion:\n\n<!-- markdownlint-disable MD033 -->\n<div style="display: flex; align-items: center; justify-content: space-between;">\n  <img src="https://raw.githubusercontent.com/d2b-dev/d2b/master/assets/autocomplete1.png" width="40%"/>\n  <img src="https://raw.githubusercontent.com/d2b-dev/d2b/master/assets/autocomplete2.png" width="40%"/>\n</div>\n<!-- markdownlint-enable MD033 -->\n\nas well as validation while you edit your config files:\n\n<!-- markdownlint-disable MD033 -->\n<div style="display: flex; align-items: center; justify-content: space-between;">\n  <img src="https://raw.githubusercontent.com/d2b-dev/d2b/master/assets/validation.png" width="40%"/>\n</div>\n<!-- markdownlint-enable MD033 -->\n\nFor example, with vscode you might create/add to your `.vscode/settings.json` file in the workspace to include:\n\n```text\n{\n  // ... other settings ...\n\n  "json.schemas": [\n    {\n      "fileMatch": ["*d2b-config*.json"],\n      "url": "https://raw.githubusercontent.com/d2b-dev/d2b/master/json-schemas/schema.json"\n    }\n  ]\n}\n```\n\nHaving this setting enabled would mean that any file matching `*d2b-config*.json` would be validated against the latest JSON schema in the [`d2b` repo](https://github.com/d2b-dev/d2b/blob/master/json-schemas/schema.json)\n\n## The plugin system\n\n`d2b` uses [`pluggy`](https://github.com/pytest-dev/pluggy) to faciliate the discorvery and integration of plugins, as such familiarity with the [pluggy documentation](https://pluggy.readthedocs.io/en/latest/) is helpful.\n\nThat said, here\'s a small example:\n\nLet\'s write a plugin that adds the command `d2b hello <name>` to `d2b`.\n\nThe convention is to name the package implementing the plugin `d2b-[plugin-name]`, so we\'ll name our package `d2b-hello`.\n\nLet\'s add the plugin implementation\n\n`d2b-hello/d2b_hello.py`:\n\n```python\nfrom __future__ import annotations\n\nimport argparse\n\nfrom d2b.hookspecs import hookimpl\n\n\n@hookimpl\ndef register_commands(subparsers: argparse._SubParsersAction):\n    parser = subparsers.add_parser("hello")\n    parser.add_argument("name", help="Greet this person")\n    parser.add_argument("--shout", action="store_true", help="Shout it!")\n    parser.set_defaults(handler=handler)\n\n\ndef handler(args: argparse.Namespace):\n    name: str = args.name\n    shout: bool | None = args.shout\n    greeting = f"Hello, {name}!"\n    print(greeting.upper() if shout else greeting)\n```\n\nThe script above is tapping into one of the various pluggable locations (hookspecs in pluggy speak) by providing and implementation (hookimpl) of one of the desired hookspecs (`register_commands`) exposed by `d2b`.\n\nThere are many spots in `d2b` which allow for a user to extend or change the core functionality. Check out the module [`hookspecs.py`](https://github.com/d2b-dev/d2b/blob/master/src/d2b/hookspecs.py) to see which hooks are available.\n\nIn the case above `register_commands` is one of the hookspecs defined by `d2b` enabling for plugins to add subcommands to the `d2b` CLI.\n\nHow do we tell `d2b` about our plugin?\n\nTo discover the plugin `d2b` (via `pluggy`) uses [entrypoints](https://pluggy.readthedocs.io/en/latest/#loading-setuptools-entry-points). So we\'ll add a basic `setup.py` module:\n\n`d2b-hello/setup.py`:\n\n```python\nfrom setuptools import find_packages\nfrom setuptools import setup\n\nsetup(\n    name="d2b-hello",\n    install_requires="d2b>=0.2.3,<1.0",\n    entry_points={"d2b": ["d2b-hello=d2b_hello"]},\n    packages=find_packages(),\n)\n```\n\nAnd now we can install our plugin:\n\n```bash\npip install -e ./d2b-hello/\n```\n\nAfter which we have:\n\n```bash\n$ d2b --help\nusage: d2b [-h] [-v] {run,scaffold,hello} ...\n\nd2b - Organize data in the BIDS format\n\npositional arguments:\n  {run,scaffold,hello}\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -v, --version         show program\'s version number and exit\n```\n\nOur `d2b hello` subcommand is there!\n\n```bash\n$ d2b hello --help\nusage: d2b hello [-h] [--shout] name\n\npositional arguments:\n  name        Greet this person\n\noptional arguments:\n  -h, --help  show this help message and exit\n  --shout     Shout it!\n```\n\nAnd, trying it out:\n\n```bash\n$ d2b hello Andrew --shout\nHELLO, ANDREW!\n```\n\nSuccess! 🏆\n\n## Contributing\n\n1. Have or install a recent version of `poetry` (version >= 1.1)\n1. Fork the repo\n1. Setup a virtual environment (however you prefer)\n1. Run `poetry install`\n1. Run `pre-commit install`\n1. Add your changes (adding/updating tests is always nice too)\n1. Commit your changes + push to your fork\n1. Open a PR\n',
    'author': 'Andrew Ross',
    'author_email': 'andrew.ross.mail@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/d2b-dev/d2b',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0',
}


setup(**setup_kwargs)

from setuptools import setup, find_packages
import os
import re


badges = """[![version](https://img.shields.io/pypi/v/<name>.svg)](https://pypi.org/project/<name>/)
[![license](https://img.shields.io/pypi/l/<name>.svg)](https://pypi.org/project/<name>/)
[![pyversions](https://img.shields.io/pypi/pyversions/<name>.svg)](https://pypi.org/project/<name>/)  
[![donate](https://img.shields.io/badge/Donate-Paypal-0070ba.svg)](https://paypal.me/foxe6)
[![powered](https://img.shields.io/badge/Powered%20by-UTF8-red.svg)](https://paypal.me/foxe6)
[![made](https://img.shields.io/badge/Made%20with-PyCharm-red.svg)](https://paypal.me/foxe6)
"""
name = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
badges = re.sub(r"<name>", name, badges)
readme = open("README.md", "rb").read().decode("utf-8")
readme = re.sub(r"(<badges>).*?(</badges>)", r"\g<1>{}\g<2>".format(badges), readme, flags=re.DOTALL)
open("README.md", "wb").write(readme.encode("utf-8"))
description = re.search(r"<i>(.*?)</i>", readme)[1]
setup(
    name="omnitools",
    version="0.0.110",
    keywords=["omnitools python utilities shortcuts misc"],
    packages=find_packages(),
    package_data={
        "": [
            "*.ttc",
            "pkg_data.json",
            "example/*.*",
            "../*.txt",
            "../*.md",
            "../LICENSE",
            "../.gitignore",
        ],
    },
    url="https://github.com/foxe6/omnitools",
    license="AGPL-3.0",
    author="f̣ộx̣ệ6",
    author_email="foxe6@protonmail.com",
    description=description,
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=open("requirements.txt").read().splitlines(),
    python_requires=">=3",
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Topic :: Utilities",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: Microsoft :: Windows :: Windows 10"
    ]
)

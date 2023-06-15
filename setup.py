#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

import os
import platform
import re
from typing import Dict

from setuptools import find_packages, setup  # type: ignore


here = os.path.abspath(os.path.dirname(__file__))
base_deps = [
    "Authlib==1.2.0",
    "dag-cbor==0.2.2",
    "jsonpatch==1.32",
    "multiformats==0.1.4.post3",
    "requests==2.28.2",
]


here = os.path.abspath(os.path.dirname(__file__))
about: Dict[str, str] = {}
with open(os.path.join(here, "ceramic", "__version__.py"), "r") as f:
    exec(f.read(), about)

def parse_readme():
    with open("README.md", "r") as f:
        readme = f.read()
    # replace relative links of images
    raw_url_root = "https://raw.githubusercontent.com/valory-xyz/ceramic-python-client/main/"
    replacement = raw_url_root + r"\g<0>"
    readme = re.sub(r"(?<=<img src=\")(/.*)(?=\")", replacement, readme, re.DOTALL)
    return "\n".join([readme])


if __name__ == "__main__":
    setup(
        name=about["__title__"],
        description=about["__description__"],
        version=about["__version__"],
        author=about["__author__"],
        url=about["__url__"],
        license=about["__license__"],
        long_description=parse_readme(),
        long_description_content_type="text/markdown",
        packages=find_packages(include=["ceramic*"]),
        classifiers=[
            "Environment :: Console",
            "Environment :: Web Environment",
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Natural Language :: English",
            "Operating System :: MacOS",
            "Operating System :: Microsoft",
            "Operating System :: Unix",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Topic :: Communications",
            "Topic :: Internet",
            "Topic :: Scientific/Engineering",
            "Topic :: Software Development",
            "Topic :: System",
        ],
        zip_safe=False,
        install_requires=base_deps,
        python_requires=">=3.8",
        project_urls={
            "Bug Reports": "https://github.com/valory-xyz/ceramic-python-client/issues",
            "Source": "https://github.com/valory/ceramic-python-client",
        },
    )

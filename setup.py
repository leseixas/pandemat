# -*- coding: utf-8 -*-
# file: setup.py

# This code is part of Pandemat
#
# Copyright (c) 2022 Leandro Seixas Rocha.
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

from setuptools import setup, find_packages
# from .pandemat.__init__ import version

# Read in requirements.txt
requirements = open('requirements.txt').readlines()
requirements = [r.strip() for r in requirements]

setup(
    name = "pandemat",
    version = "0.0.1",
    packages = find_packages(),
    author = "Leandro Seixas",
    author_email = "leandro.seixas@mackenzie.br", 
    url="https://macksim.org/pandemat",
    description = "(Under development). Pandemat is a tool for high-entropy materials calculations and data analysis.",
    long_description='''
    (Under development). Pandemat is a tool for high-entropy materials calculations and data analysis.
    ''',
    install_requires = requirements,
    license = 'Apache 2',
    classifiers = [
         "Development Status :: 1 - Planning",
         "Programming Language :: Python :: 3",
         "Topic :: Scientific/Engineering :: Chemistry",
         "Topic :: Scientific/Engineering :: Physics",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent"
    ],
    python_requires = '>= 3.7.*'
)

#   Filename:       setup.py
#   Description:    The setup.py is the centre of all activity in building, distributing, and installing modules using the Distutils.
#
#   Copyright (C) 2020 Shyam Singh
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

import setuptools


setuptools.setup(
    name="UnoGame",
    version="0.0.1",
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    author="Shyam Singh",
    author_email="shyam81295@gmail.com",
    url="https://github.com/shyam81295/UnoGame",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="To improve Software Engineer skills, creating this UNO Game to learn OOPS, Low-level Design, System Design(High-Level Design), Scalability, FrontEnd, BackEnd, DB, Distributed Systems, etc. Understanding of software components like CI/CD, automated testing, etc.",
    entry_points={},
    data_files=[],
)

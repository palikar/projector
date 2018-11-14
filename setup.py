#!/usr/bin/env python3
import os
import sys
import setuptools
import glob
from distutils.core import setup


if sys.version_info < (3, 3):
    print("THIS MODULE REQUIRES PYTHON 3.3+. YOU ARE CURRENTLY\
    USING PYTHON {0}".format(sys.version))
    sys.exit(1)

    

exec(open('projector/version.py').read())

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

extra_files = package_files('./projector/data/')

setup(
    name="Projector",
    version=__version__,
    # package_data={'projector': data_files},
    package_data={'': extra_files},
    include_package_data=True,
    author="Stanislav Arnaudov",
    author_email="stanislav_ts@abv.bg",
    description="Tool for easy project creation from templates.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="GNU General Public License v3.0",
    keywords="projects management generator",
    url="https://github.com/palikar/projector",
    setup_requires=["pytest-runner", "pystache"],
    tests_require=["pytest"],
    entry_points={
        'console_scripts': [
            'projector = projector.create_project:main'
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Installation/Setup"
    ],
)

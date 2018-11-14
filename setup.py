#!/usr/bin/env python3
import sys
import setuptools
from distutils.core import setup


if sys.version_info < (3, 3):
    print("THIS MODULE REQUIRES PYTHON 3.3+. YOU ARE CURRENTLY\
    USING PYTHON {0}".format(sys.version))
    sys.exit(1)


exec(open('projector/version.py').read())

setup(
    name="Projector",
    version=__version__,
    package_data={'projector': ['data/*']},
    include_package_data=True,
    author="Stanislav Arnaudov",
    author_email="stanislav_ts@abv.bg",
    description="Tool for easy peoject creation from templates.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="GNU General Public License v3.0",
    keywords="projects management generator",
    url="https://github.com/palikar/projector",
    setup_requires=["pytest-runner", "pystache"],
    tests_require=["pytest"],
    entry_points={
        'console_scripts': []
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

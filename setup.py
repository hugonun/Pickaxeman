from setuptools import setup
import os
import sys

import pickaxeman

py_version = sys.version_info[:2]

if py_version < (3, 5):
    raise Exception("pickaxeman requires Python >= 3.5.")

here = os.path.abspath(os.path.dirname(__file__))

with open('requirements.txt') as f:
    dependencies = f.read().splitlines()

long_description = """
Pickaxeman uses co-routines and multiprocessing to download and process certificates from a Certificate Transparency
List and outputs them. It is intended to be a local version of certstream, but turned into a Python lib.
"""

setup(
    name='pickaxeman',
    version=axeman.__version__,
    url='https://github.com/hugonun/Pickaxeman/',
    author='Hugo Nunes',
    install_requires=dependencies,
    description='Pickaxeman is a multi-threaded and concurrent certificate transparency retriever.',
    long_description=long_description,
    packages=['pickaxeman'],
    include_package_data=True,
    license = "MIT",
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Testing",
        "Environment :: Console",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
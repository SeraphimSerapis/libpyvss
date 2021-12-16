#!/usr/bin/env python3

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='vss-python-api',
    version='0.9.7',
    url='https://github.com/SeraphimSerapis/libpyvss.git',
    author='Tim Messerschmidt',
    description='A fork of the official libpyvss',
    packages=find_packages(),
    install_requires=['requests', 'requests-toolbelt', 'python-dotenv'],
)

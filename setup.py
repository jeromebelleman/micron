#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='micron',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Schedule jobs",
    long_description="Resiliently schedule jobs.",
    scripts=['micron'],
    data_files=[('share/man/man1', ['micron.1'])],
)

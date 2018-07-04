#!/usr/bin/env python

from setuptools import setup, find_packages
from os.path import dirname, join, relpath

CURDIR = dirname(relpath(__file__))

with open(join(CURDIR, 'requirements.txt')) as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name                = 'robotframework-javaproperties',
    version             = '0.1',
    description         = 'Java properties files library for Robot Framework',
    author              = 'Arne Wohletz',
    author_email        = 'a.wohletz@erhardt-leimer.com',
    url                 = 'https://no/url',
    license             = 'Apache License 2.0',
    keywords            = 'robotframework javaproperties testautomation',
    platforms           = 'any',
    package_dir         = {'': 'src'},
    packages            = find_packages('src'),
    install_requires    = REQUIREMENTS,
    setup_requires      = ["pytest-runner"],
    tests_require       = ["pytest"],

)

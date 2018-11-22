#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
setup(name='hueglucose',
    version = '1.0.0',
    url = 'https://github.com/dabear/hueglucose.git',
    author = 'Bjorn Berg',
    author_email = 'bjorninges.spam@gmail.com',
    description = 'Sets up a philips hue to display different lighting based on nightscout glucose values',
    packages = find_packages(),
    install_requires=[
        'python-nightscout',
        'phue',
        'pytz'
    ],
    dependency_links=[
        'https://github.com/ps2/python-nightscout/tarball/master#egg=python-nightscout-1.0.0',
        
    ],
    
)

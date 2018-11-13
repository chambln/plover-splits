#!/usr/bin/env python3

from setuptools import setup


setup(
    name = 'plover_splits',
    version = '0.0.1',
    description = 'System for Plover that divides the left hand S',
    author = 'Gregory Chamberlain',
    author_email = 'chambln@pm.me',
    license =  'GNU General Public License v2 or later (GPLv2+)',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires = [
        'plover>=4.0.0.dev0',
    ],
    packages = [
        'plover_splits',
    ],
    entry_points = '''

    [plover.system]
    Plover Splits = plover_splits.system

    ''',
    include_package_data = True,
    zip_safe = True,
)

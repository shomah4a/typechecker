#-*- coding:utf-8 -*-

import setuptools
import typechecker

version = '0.1.0'

setuptools.setup(
    name='typechecker',
    version=typechecker.__version__,
    packages=['typechecker'],
    install_requires=[
        ],
    author=typechecker.__author__,
    author_email='shoma.h4a+pypi@gmail.com',
    license=typechecker.__license__,
    url='https://github.com/shomah4a/typechecker',
    description='This module provides dynamic type check mechanism.',
    long_description=typechecker.__doc__,
    classifiers='''
Programming Language :: Python
Development Status :: 2 - Pre-Alpha
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Utilities
'''.strip().splitlines())

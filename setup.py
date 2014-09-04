#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""\
SmartyPants: a smart-quotes plugin.

This module encapsulates Chad Miller's SmartyPants module so that
it's available on PyPI. For more information, consult

* http://web.chad.org/projects/smartypants.py/
* http://daringfireball.net/projects/smartypants/

The first two version numbers are Chad Miller's. The last two are
mine.

This is a Bond fork of SmartyPants (with unicode support!).

"""

# All of this is adapted from markdown2's setup.py.
# from distutils.core import setup
# Use setuptools instead
from setuptools import setup

doclines = __doc__.split("\n")
classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Programming Language :: Python
Operating System :: OS Independent
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Documentation
Topic :: Text Processing :: Filters
"""

setup(
    name = 'bond-smartypants',
    version = '1.5_2.0',
    author = 'Chad Miller',
    maintainer = "Anthony O'Brien",
    maintainer_email = "anthony@bond{spam=NO!}gifts.com",
    url = 'http://web.chad.org/projects/smartypants.py/',
    license = 'BSD',
    platforms = ['any'],
    py_modules = ['smartypants'],
    package_dir = {'': 'lib'},
    #scripts=[script],
    description = doclines[0],
    classifiers = filter(None, classifiers.split("\n")),
    long_description = "\n".join(doclines[2:]),
)

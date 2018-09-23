#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File defines metadata, modules and packages for this distribution so that `python setup.py sdist` will create
a distribution (compressed tar file) for current project.
"""

from setuptools import setup, find_packages

'''
Import README.rst for Setup Object: Usually long strings  (long_description) needs .rst
file but as .md content is same as will be in .rst - Using same
'''
with open('README.md') as f:
    readme = f.read()

'''
Import LICENSE for Setup Object: Usually short strings  (license) needs .txt files.
'''
with open('LICENSE') as f:
    license = f.read()

"""
Adding Packaging Information:

- Version: Encoding the version information is an art in itself. Python packages generally adhere to the
version format major.minor[.patch][sub]. The major number is 0 for initial, experimental releases
of software. It is incremented for releases that represent major milestones in a package. The minor
number is incremented when important new features are added to the package. The patch number increments
when bug-fix releases are made. Additional trailing version information is sometimes used to indicate
sub-releases. These are “a1,a2,…,aN” (for alpha releases, where functionality and API may change), “b1,b2,…,bN”
(for beta releases, which only fix bugs) and “pr1,pr2,…,prN” (for final pre-release release testing).

- Classifier: Needs to define development status, enviornment, intended audiance, license, operating system,
programming language, etc.
"""
setup(name='sg-downloader',
    version='0.0.0dev1',
    description='Universal course, video & url downloader',
    long_description=readme,
    author='Sachin Gupta',
    author_email='sachin.aut@gmail.com',
    maintainer='Sachin Gupta',
    maintainer_email='sachin.aut@gmail.com',
    url='https://github.com/sachin-gupta/sg-downloader',
    license=license,
    download_url='https://github.com/sachin-gupta/sg-downloader',
    classifiers=[
        'Development Status :: 1 - Dev',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Software :: Download Manager',
    ],
    packages=find_packages(exclude=('tests', 'docs'))
    )

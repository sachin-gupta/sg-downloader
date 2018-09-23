#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='sg-downloader',
    version='1.0.0',
    description='Universal course, video & url downloader',
    long_description=readme,
    author='Sachin Gupta',
    author_email='sachin.aut@gmail.com',
    url='https://github.com/sachin-gupta/sg-downloader',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
    )

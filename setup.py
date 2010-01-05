#!/usr/bin/env python
# encoding: utf-8

'Using the markItUp! Rich Text Editor for Textile Markup for Django'

from setuptools import setup, find_packages
import codecs

setup(name='django-markitup',
      maintainer='Maximillian Dornseif',
      maintainer_email='md@hudora.de',
      url='https://github.com/hudora/django-markitup',
      version='0.02',
      description=__doc__,
      long_description=codecs.open('README.rst', "r", "utf-8").read(),
      classifiers=['License :: OSI Approved :: BSD License',
                   'Intended Audience :: Developers',
                   'Programming Language :: Python'],
      zip_safe=False,
      packages = find_packages('markitup'),
      install_requires=['Django'],
)

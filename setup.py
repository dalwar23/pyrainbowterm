#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Dalwar Hossain'
__email__ = 'dalwar.hossain@protonmail.com'


from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='xtermcolors',
      version='1.0',
      description='xtermcolors - Smart custom print function with color and log information support',
      long_description=readme(),
      classifiers=[
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='terminal colors xterm python colored output',
      url='https://github.com/dharif23/xtermcolors',
      author='Dalwar Hossain',
      author_email='dalwar.hossain@protonmail.com',
      license='MIT',
      packages=['xtermcolors'],
      # install_requires=[
      #    'markdown',
      # ],
      # test_suite='nose.collector',
      # tests_require=['nose', 'nose-cover3'],
      # entry_points={
      #    'console_scripts': ['funniest-joke=funniest.command_line:main'],
      # },
      include_package_data=True,
      zip_safe=False)
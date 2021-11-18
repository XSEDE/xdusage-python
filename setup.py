import os
from setuptools import setup
from setuptools import find_packages

def readme():
    with open("README.md") as f:
        return f.read()

setup(name='xdusage',
      version='1.0',
      scripts=['bin/xdusage','bin/xdusage_v1.py', 'bin/xdusage_v2.py'],
      )

# -*- coding: utf-8 -*-

import sys

if 'bdist_wheel' in sys.argv:
    # to build wheel, use 'python setup.py sdist bdist_wheel'
    from setuptools import setup
else:
    from distutils.core import setup # 'python setup.py install'

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
__version__ = None
with open('./chncal/__init__.py', 'r', encoding='utf-8') as f:
    exec(f.readlines()[4].strip())

setup(
    name='chncal',
    version=__version__,
    description='Chinese calendar toolkit.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Genlovy Hoo',
    author_email='genlovhyy@163.com',
    url='https://gitcode.com/glhyyz/ChnCal',
    license='MIT License',
    install_requires=['dramkit'],
    packages=['chncal',
              'chncal.constants',
              'chncal.constant_creator'],
)

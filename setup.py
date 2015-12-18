# -*- coding: utf-8 -*-
from setuptools import setup
import io


setup(
    author=u'Kiss György',
    author_email='kissgyorgy@me.com',
    url='https://github.com/Walkman/pytest_raisesregexp',
    description='Simple pytest plugin to look for regex in Exceptions',
    long_description=io.open('README.rst', encoding='utf-8').read(),
    name='pytest-raisesregexp',
    packages=['pytest_raisesregexp'],
    version='2.1',
    install_requires=['py', 'pytest'],
    # the following makes a plugin available to py.test
    entry_points={
        'pytest11': [
            'raises_regexp = pytest_raisesregexp.plugin',
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Testing'
    ]
)

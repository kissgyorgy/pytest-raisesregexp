from setuptools import setup


setup(
    author='Walkman',
    author_email='kissgyorgy@me.com',
    url='https://github.com/Walkman/pytest_raisesregexp',
    description='Simple pytest plugin to look for regex in Exceptions',
    long_description=open('README.rst').read(),
    name='pytest-raisesregexp',
    packages=['pytest_raisesregexp'],
    version='1.0',
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
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing'
    ]
)

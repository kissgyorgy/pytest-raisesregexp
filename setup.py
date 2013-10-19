from setuptools import setup

setup(
    author="Walkman",
    author_email="kissgyorgy@me.com",
    name="pytest-raisesregexp",
    packages=['pytest_raisesregexp'],
    version="0.1.0",
    install_requires=['py', 'pytest'],
    # the following makes a plugin available to py.test
    entry_points={
        'pytest11': [
            'raises_regexp = pytest_raisesregexp.plugin',
        ]
    },
)


pytest-raisesregexp
===================

|travis| |pythons| |release| |license| |downloads| |wheel|

I really missed `assertRaisesRegexp` in unittest module from ``pytest``,
so I wrote this simple plugin.

Usage
-----

.. code-block:: python

    # some_module.py
    class ExpectedException(Exception):
    	pass

    def function_to_test():
    	raise ExpectedException('error message: 1560')


.. code-block:: python

    # test_some_module.py
    from pytest import raises_regexp
    from some_module import function_to_test, ExpectedException

    def test_something_to_test():
        with raises_regexp(ExpectedException, r".* 1560"):
            function_to_test()


Installation
------------

.. code-block:: bash

    $ pip install pytest-raisesregexp

It installs as a pytest entry point, so you can:

.. code-block:: python

    from pytest import raises_regexp


LICENSE
-------

MIT license
Copyright (c) 2013-2014 Kiss György


.. |travis| image:: https://travis-ci.org/Walkman/pytest-raisesregexp.svg?branch=master
    :target: https://travis-ci.org/Walkman/pytest-raisesregexp

.. |pythons| image:: https://pypip.in/py_versions/pytest-raisesregexp/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/pytest-raisesregexp/
   :alt: Supported Python versions

.. |release| image:: https://pypip.in/version/pytest-raisesregexp/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/pytest-raisesregexp/
   :alt: Latest Version

.. |license| image:: https://pypip.in/license/pytest-raisesregexp/badge.svg?style=flat
   :target: https://github.com/Walkman/pytest-raisesregexp/blob/master/LICENSE
   :alt: MIT License

.. |downloads| image:: https://pypip.in/download/pytest-raisesregexp/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/pytest-raisesregexp/
   :alt: Downloads

.. |wheel| image:: https://pypip.in/wheel/pytest-raisesregexp/badge.svg?style=flat
   :target: https://pypi.python.org/pypi/pytest-raisesregexp/
   :alt: Wheel package

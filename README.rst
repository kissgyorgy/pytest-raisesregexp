pytest-raisesregexp
===================

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

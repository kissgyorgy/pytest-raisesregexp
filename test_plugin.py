# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
from pytest import raises_regexp


class ExpectedException(Exception):
    pass


def function_to_test():
    raise ExpectedException('error message: 1560')


def function_to_test_with_args(arg1, arg2):
    raise ExpectedException('Arg params: {0}, {1}'.format(arg1, arg2))


def _function_to_test_with_kwargs(kwarg1='kw1', kwarg2='kw2'):
    raise ExpectedException('Kwarg params: {0}, {1}', kwarg1, kwarg2)


def function_to_test_with_args_and_kwargs(*args, **kwargs):
    raise ExpectedException('Args and kwargs raised: {0}, {1}'.format(args, kwargs))



def test_simple():
    with raises_regexp(ExpectedException, r".* 1560"):
        function_to_test()


def test_pytest_namespace():
    with pytest.raises_regexp(ExpectedException, r".* 1560"):
        function_to_test()


def test_full_match_passes():
    with raises_regexp(ExpectedException, 'error message: 1560'):
        function_to_test()


def test_function_with_args():
    with raises_regexp(ExpectedException, 'Arg params: 1, 2'):
        function_to_test_with_args(1, 2)


def test_functional_syntax():
    raises_regexp(
        ExpectedException,
        r"Args and kwargs raised: .*param1.*param4",
        function_to_test_with_args_and_kwargs,
        'param1', 'param2', kwarg1='param3', kwarg2='param4'
    )


def test_functional_syntax_without_args_or_kwargs():
    raises_regexp(ExpectedException, r'.* 1560', function_to_test)



# pytest-raisesregexp
I really missed `assertRaisesRegexp` in unittest module from `pytest`, but as I don't want to use unittest anymore :smile: I wrote this simple plugin for `pytest`.

## Usage:

```python

# some_module.py  
class ExpectedException():
	pass

def function_to_test():
	raise ExpectedException('error message: 1560')
```

```python
# test_some_module.py  
from pytest import raises_regexp
from some_module import function_to_test, ExpectedException

def test_something_to_test():
    with raises_regexp(ExpectedException, r".* 1560"):
        function_to_test()
```

## Install:
`$ python setup.py install`

## LICENSE

MIT license
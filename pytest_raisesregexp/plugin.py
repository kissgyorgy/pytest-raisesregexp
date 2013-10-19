import re
import py.code
import pytest


def pytest_namespace():
    return {'raises_regexp': raises_regexp}


class raises_regexp(object):
    def __init__(self, expected_exception, regexp):
        self.exception = expected_exception
        self.regexp = regexp
        self.excinfo = None

    def __enter__(self):
        self.excinfo = object.__new__(py.code.ExceptionInfo)
        return self.excinfo

    def __exit__(self, exc_type, exc_val, exc_tb):
        __tracebackhide__ = True
        if exc_type is None:
            pytest.fail('DID NOT RAISE %s' % self.exception)

        self.excinfo.__init__((exc_type, exc_val, exc_tb))

        if not issubclass(exc_type, self.exception):
            pytest.fail('%s RAISED instead of %s\n%s' % (exc_type, self.exception, repr(exc_val)))

        if not re.search(self.regexp, str(exc_val)):
            pytest.fail('pattern "%s" not found in "%s"' % (self.regexp, str(exc_val)))

        return True

import unittest
from os.path import dirname
from unittest.runner import TextTestResult

from tests import pybots


def main():
    loader = unittest.TestLoader()

    suite = loader.discover(dirname(pybots.__file__), pattern='*.py')
    result = unittest.TextTestRunner(verbosity=10).run(unittest.TestSuite(suite))
    assert isinstance(result, TextTestResult)
    exit(len(result.errors + result.failures))


if __name__ == '__main__':
    main()
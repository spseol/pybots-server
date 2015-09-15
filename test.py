import unittest
from os.path import dirname

from tests import pybots


if __name__ == '__main__':
    loader = unittest.TestLoader()

    suite = loader.discover(dirname(pybots.__file__), pattern='*.py')
    unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(suite))
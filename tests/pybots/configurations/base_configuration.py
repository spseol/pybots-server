from pybots.configurations.base_configuration import BaseConfiguration, ConfigurationError
from tests.test_case import TestCase


class TestBaseConfiguration(TestCase):
    def test_init(self):
        class Conf(BaseConfiguration):
            _fields = (
                ('bar', int),
            )
            bar = 'foo'

        with self.assertRaises(ConfigurationError):
            Conf()

        class Conf(BaseConfiguration):
            _fields = (
                ('bar', int),
                ('foo', )
            )
            bar = 5

        with self.assertRaises(ConfigurationError):
            Conf()

        class Conf(BaseConfiguration):
            _fields = (
                ('bar', int),
            )
            bar = None

        with self.assertRaises(ConfigurationError):
            Conf()



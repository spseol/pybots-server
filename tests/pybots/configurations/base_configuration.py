from pybots.configurations.base_configuration import BaseConfiguration, ConfigurationError
from pybots.configurations.random_field_placer import RandomFieldPlacerMixin
from tests.test_case import TestCase


class TestBaseConfiguration(TestCase):
    def test_init(self):
        class Conf(BaseConfiguration, RandomFieldPlacerMixin):
            _fields = (
                ('bar', int),
            )
            bar = 'foo'

        with self.assertRaises(ConfigurationError):
            Conf()

        class Conf(BaseConfiguration, RandomFieldPlacerMixin):
            _fields = (
                ('bar', int),
                ('foo', None)
            )
            bar = 5

        with self.assertRaises(ConfigurationError):
            Conf()

        class Conf(BaseConfiguration, RandomFieldPlacerMixin):
            _fields = (
                ('bar', int),
            )
            bar = None

        with self.assertRaises(ConfigurationError):
            Conf()

    def test_lambda_fields(self):
        class Conf(BaseConfiguration, RandomFieldPlacerMixin):
            _fields = (
                ('bar', int),
            )
            bar = lambda: 'foo'

        with self.assertRaises(ConfigurationError):
            Conf()




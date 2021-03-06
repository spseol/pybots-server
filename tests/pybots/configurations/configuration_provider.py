from pybots.configurations.base_configuration import BaseConfiguration
from pybots.configurations.configuration_provider import configuration_provider
from pybots.configurations.random_field_placer import RandomFieldPlacerMixin
from tests.test_case import TestCase


class TestConfigurationProvider(TestCase):
    def test_actual(self):
        self.assertIsInstance(configuration_provider.actual, BaseConfiguration)
        self.assertIsInstance(configuration_provider.actual, configuration_provider.DEFAULT_CONFIGURATION)

    def test_set_actual(self):
        with self.assertRaises(AssertionError):
            configuration_provider.actual = None

        class MyConf(BaseConfiguration, RandomFieldPlacerMixin):
            _fields = dict()

        my_conf = MyConf()
        configuration_provider.actual = my_conf
        self.assertIs(configuration_provider.actual, my_conf, 'Set configuration as actual.')
        configuration_provider._actual = None
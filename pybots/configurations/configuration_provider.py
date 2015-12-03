from pybots.configurations.base_configuration import BaseConfiguration
from pybots.configurations.default_configuration import DefaultConfiguration


class ConfigurationProvider(object):
    DEFAULT_CONFIGURATION = DefaultConfiguration

    def __init__(self):
        self._actual = None

    @property
    def actual(self):
        if not self._actual:
            self._actual = self.DEFAULT_CONFIGURATION()
        return self._actual

    @actual.setter
    def actual(self, configuration):
        assert isinstance(configuration, BaseConfiguration)
        self._actual = configuration


configuration_provider = ConfigurationProvider()

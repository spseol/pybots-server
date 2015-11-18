from pybots.configurations.base_configuration import BaseConfiguration
from pybots.configurations.random_configuration import RandomConfiguration


class ConfigurationProvider(object):
    DEFAULT_CONFIGURATION = RandomConfiguration

    def __init__(self):
        self._actual = None

    @property
    def actual(self):
        if not self._actual:
            self._actual = self.DEFAULT_CONFIGURATION()
            # raise ConfigurationError('')
        return self._actual

    @actual.setter
    def actual(self, configuration):
        assert isinstance(configuration, BaseConfiguration)
        self._actual = configuration


configuration_provider = ConfigurationProvider()

from pybots.configurations.base_configuration import BaseConfiguration
from pybots.configurations.default_configuration import DefaultConfiguration
from pybots.configurations.random_field_placer import RandomFieldPlacerMixin


class CustomConfiguration(BaseConfiguration, RandomFieldPlacerMixin):
    default_empty_map_field = DefaultConfiguration.default_empty_map_field

    def __init__(self, **kwargs):
        field_names = tuple(self._fields.keys())
        for key, value in kwargs.items():
            if key in field_names:
                setattr(self, key, value)
        super(BaseConfiguration, self).__init__()

from _operator import itemgetter

from pybots.configurations.base_configuration import BaseConfiguration
from pybots.configurations.basic_configuration import DefaultConfiguration


class CustomConfiguration(BaseConfiguration):
    default_empty_map_field = DefaultConfiguration.default_empty_map_field

    def __init__(self, **kwargs):
        field_names = tuple(map(itemgetter(0), self._fields))
        for key, value in kwargs.items():
            if key in field_names:
                setattr(self, key, value)
        super().__init__()

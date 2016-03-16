from pybots.configurations.base_configuration import BaseConfiguration
from pybots.configurations.random_field_placer import RandomFieldPlacerMixin
from pybots.game.fields.empty_field import EmptyField


class DefaultConfiguration(BaseConfiguration, RandomFieldPlacerMixin):
    map_width = 70
    map_height = 50
    default_empty_map_field = EmptyField
    bots = 2
    treasures = 1
    blocks = 1000

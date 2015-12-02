from pybots.configurations.base_configuration import BaseConfiguration
from pybots.game.fields.empty_field import EmptyField


class DefaultConfiguration(BaseConfiguration):
    map_width = 10
    map_height = 8
    default_empty_map_field = EmptyField
    bots = 2
    treasures = 1
    blocks = 10

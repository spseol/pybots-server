from random import randint

from pybots.configurations.base_configuration import BaseConfiguration
from pybots.game.fields.empty_field import EmptyField


class RandomConfiguration(BaseConfiguration):
    map_width = lambda: randint(10, 100)
    map_height = lambda: randint(10, 100)
    default_empty_map_field = EmptyField
    bots = 2
    treasures = 1
    blocks = lambda: randint(50, 75)

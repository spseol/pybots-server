import random

from pybots.configurations.base_configuration import BaseConfiguration
from pybots.game.fields.empty_field import EmptyField


class RandomConfiguration(BaseConfiguration):
    map_width = lambda: random.randint(10, 100)
    map_height = lambda: random.randint(10, 100)
    default_empty_map_field = EmptyField
    bots = 2
    treasures = 1
    blocks = lambda: random.randint(50, 75)

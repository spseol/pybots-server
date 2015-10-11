import random

from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map import Map
from pybots.game.orientations import Orientation


class MapFactory(object):
    BOTS = 1
    TREASURES = 1

    def __init__(self, bots=BOTS, treasures=TREASURES, **kwargs):
        self.map_options = kwargs
        self.bots = bots
        self.treasures = treasures

    def create(self):
        game_map = Map(**self.map_options)

        def random_position():
            return random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1)

        for _i in range(self.treasures):
            treasure = TreasureField()
            position = random_position()
            while not isinstance(game_map[position], EmptyField):
                position = random_position()
            game_map[position] = treasure

        for _i in range(self.bots):
            bot = BotField(Orientation.NORTH)
            position = random_position()
            while not isinstance(game_map[position], EmptyField):
                position = random_position()
            game_map[position] = bot

        return game_map

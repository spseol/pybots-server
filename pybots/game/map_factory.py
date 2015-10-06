from random import randint

from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map import Map
from pybots.game.orientations import Orientation


class MapFactory(object):
    def __init__(self, **kwargs):
        self.map_options = kwargs

    def create(self):
        game_map = Map(**self.map_options)

        def random_position():
            return randint(0, game_map.width - 1), randint(0, game_map.height - 1)

        treasure = TreasureField()

        game_map[random_position()] = treasure

        for _i in range(2):
            bot = BotField(Orientation.NORTH)
            position = random_position()
            while not isinstance(game_map[position], EmptyField):
                position = random_position()

            game_map[position] = bot

        return game_map

from random import randint

from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.player_field import PlayerField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map import Map
from pybots.game.orientations import Orientation


class MapFactory(object):
    def __init__(self, **kwargs):
        self.map_kwargs = kwargs

    def create(self):
        game_map = Map(**self.map_kwargs)

        def random_position():
            return randint(0, game_map.width - 1), randint(0, game_map.height - 1)

        treasure = TreasureField()

        game_map[random_position()] = treasure

        for _i in range(2):
            player = PlayerField(Orientation.NORTH)
            position = random_position()
            while not isinstance(game_map[position], EmptyField):
                position = random_position()

            game_map[position] = player

        return game_map

from random import choice

from pybots.configurations.base_configuration import ConfigurationError
from pybots.configurations.field_placer import FieldPlacerMixin
from pybots.game.fields.block_field import BlockField
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map import OutOfMapError, Map
from pybots.game.orientations import Orientation
from pybots.game.utils import random_position, get_next_position


class MazeFieldPlacerMixin(FieldPlacerMixin):
    default_empty_map_field = None
    maze_game = True

    def place_bots(self, game_map=None, count=None, field_class=BotField, *args, **kwargs):
        self._check_place_args(game_map, count, field_class)
        for _i in range(count):
            bot = field_class(Orientation.NORTH)
            position = random_position(game_map)
            while not isinstance(game_map[position], self.default_empty_map_field):
                position = random_position(game_map)
            game_map[position] = bot

    def place_treasures(self, game_map=None, count=None, field_class=TreasureField, *args, **kwargs):
        self._check_place_args(game_map, count, field_class)
        for _i in range(count):
            treasure = field_class()
            position = random_position(game_map)
            while not isinstance(game_map[position], self.default_empty_map_field):
                position = random_position(game_map)
            game_map[position] = treasure

    def place_blocks(self, game_map=None, count=None, field_class=BlockField, *args, **kwargs):
        self._check_place_args(game_map, count, field_class)
        assert isinstance(game_map, Map)
        bases = set()

        # TODO: frequency of blocks, constant or configuration?
        for y, row in list(enumerate(game_map))[1:-1:2]:
            for x, _ in list(enumerate(row))[1:-1:2]:
                bases.add((x, y))

        def place_blocks_line(position, orientation):
            blocks = 0
            max_blocks = len(game_map.map if orientation in (Orientation.NORTH, Orientation.SOUTH) else game_map.map[0]) / 5
            max_blocks -= max_blocks % 2
            while blocks < max_blocks:
                # TODO: as constant or configuration?
                game_map[position] = field_class()
                position = get_next_position(position, orientation)
                blocks += 1

                try:
                    field = game_map[position]
                except OutOfMapError:
                    return
                # TODO: probability of wall crossing, constant or configuration?
                if isinstance(field, field_class):
                    return
                if position in bases:
                    bases.remove(position)

        while bases:
            base = bases.pop()
            place_blocks_line(base, choice(tuple(Orientation._member_map_.values())))

    @staticmethod
    def _check_place_args(game_map, count, field_class):
        if game_map is None or count is None or field_class is None:
            raise ConfigurationError('Given parameters for placing methods is not valid.')

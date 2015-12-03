from pybots.configurations.base_configuration import ConfigurationError
from pybots.configurations.field_placer import FieldPlacerMixin
from pybots.game.fields.block_field import BlockField
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.orientations import Orientation
from pybots.game.utils import random_position


class RandomFieldPlacerMixin(FieldPlacerMixin):
    default_empty_map_field = None

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
        for _i in range(count):
            block = field_class()
            position = random_position(game_map)
            while not isinstance(game_map[position], self.default_empty_map_field):
                position = random_position(game_map)
            game_map[position] = block

    @staticmethod
    def _check_place_args(game_map, count, field_class):
        if game_map is None or count is None or field_class is None:
            raise ConfigurationError('Given parameters for placing methods is not valid.')

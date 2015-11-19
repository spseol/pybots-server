from pybots.configurations.base_configuration import BaseConfiguration
from pybots.game.fields.block_field import BlockField
from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map import Map
from pybots.game.orientations import Orientation
from pybots.game.utils import random_position


class MapFactory(object):
    def create(self, conf):
        assert isinstance(conf, BaseConfiguration)
        game_map = Map(width=conf.map_width,
                       height=conf.map_height,
                       default_field=conf.default_empty_map_field)

        if game_map.width * game_map.height < sum((conf.bots, conf.treasures, conf.blocks)):
            raise InvalidMapError('Cannot place {} bots, {} treasures and {} blocks into {}x{} map.'
                                  .format(conf.bots, conf.treasures, conf.blocks, game_map.width, game_map.height))

        for _i in range(conf.treasures):
            treasure = TreasureField()
            position = random_position(game_map)
            while not isinstance(game_map[position], EmptyField):
                position = random_position(game_map)
            game_map[position] = treasure

        for _i in range(conf.bots):
            bot = BotField(Orientation.NORTH)
            position = random_position(game_map)
            while not isinstance(game_map[position], EmptyField):
                position = random_position(game_map)
            game_map[position] = bot

        self._place_blocks_to_map(game_map, blocks=conf.blocks)
        return game_map

    def _place_blocks_to_map(self, game_map, blocks):
        for _i in range(blocks):
            block = BlockField()
            position = random_position(game_map)
            while not isinstance(game_map[position], EmptyField):
                position = random_position(game_map)
            game_map[position] = block


class InvalidMapError(Exception):
    pass

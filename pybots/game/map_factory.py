import random

from pybots.configurations.base_configuration import BaseConfiguration
from pybots.game.fields.block_field import BlockField
from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map import Map
from pybots.game.orientations import Orientation


class MapFactory(object):
    def create(self, conf):
        assert isinstance(conf, BaseConfiguration)
        game_map = Map(width=conf.map_width,
                       height=conf.map_height,
                       default_field=conf.default_empty_map_field)

        if game_map.width * game_map.height < sum((conf.bots, conf.treasures, conf.blocks)):
            raise InvalidMapError('Cannot place {} bots, {} treasures and {} blocks into {}x{} map.'
                                  .format(conf.bots, conf.treasures, conf.blocks, game_map.width, game_map.height))

        def random_position():
            return random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1)

        for _i in range(conf.treasures):
            treasure = TreasureField()
            position = random_position()
            while not isinstance(game_map[position], EmptyField):
                position = random_position()
            game_map[position] = treasure

        for _i in range(conf.bots):
            bot = BotField(Orientation.NORTH)
            position = random_position()
            while not isinstance(game_map[position], EmptyField):
                position = random_position()
            game_map[position] = bot

        for _i in range(conf.blocks):
            block = BlockField()
            position = random_position()
            while not isinstance(game_map[position], EmptyField):
                position = random_position()
            game_map[position] = block

        return game_map


class InvalidMapError(Exception):
    pass

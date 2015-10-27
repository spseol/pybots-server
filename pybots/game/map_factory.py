import random

from pybots.game.fields.block_field import BlockField
from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.bot_field import BotField

from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map import Map
from pybots.game.orientations import Orientation


class MapFactory(object):
    BOTS = 2
    TREASURES = 1
    BLOCKS = 5
    MAP_WIDTH = 13
    MAP_HEIGHT = 11

    def __init__(self, bots=BOTS, treasures=TREASURES, blocks=BLOCKS, **kwargs):
        kwargs.setdefault('width', self.MAP_WIDTH)
        kwargs.setdefault('height', self.MAP_HEIGHT)
        self.map_options = kwargs
        self.bots = bots
        self.treasures = treasures
        self.blocks = blocks

    def create(self):
        game_map = Map(**self.map_options)

        if game_map.width * game_map.height < sum((self.bots, self.treasures, self.blocks)):
            raise Exception('Cannot place {} bots, {} treasures and {} blocks into {}x{} map.'
                            .format(self.bots, self.treasures, self.blocks, game_map.width, game_map.height))

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

        for _i in range(self.blocks):
            block = BlockField()
            position = random_position()
            while not isinstance(game_map[position], EmptyField):
                position = random_position()
            game_map[position] = block

        return game_map

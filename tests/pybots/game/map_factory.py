from unittest.mock import patch

from pybots.configurations import ConfigurationError
from pybots.configurations.base_configuration import BaseConfiguration
from pybots.configurations.custom_configuration import CustomConfiguration
from pybots.configurations.random_field_placer import RandomFieldPlacerMixin
from pybots.game.fields.block_field import BlockField
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map_factory import MapFactory
from tests.test_case import TestCase


class TestMapFactory(TestCase):
    def test_create_basic(self):
        factory = MapFactory

        class Conf(BaseConfiguration, RandomFieldPlacerMixin):
            map_width = 20
            map_height = 10
            bots = 2
            treasures = 1
            blocks = 10

        conf = Conf()
        game_map = factory.create(conf)

        self.assertIsInMap(game_map, TreasureField)
        self.assertIsInMap(game_map, BotField, conf.bots)
        self.assertIsInMap(
            game_map,
            EmptyField,
            game_map.width * game_map.height - conf.bots - conf.treasures - conf.blocks
        )

    def test_create_small_map(self):
        factory = MapFactory
        conf = CustomConfiguration(map_width=5, map_height=1, bots=2, treasures=2, blocks=1)
        with patch('random.randint', side_effect=(0, 0,
                                                  0, 0,
                                                  1, 0,
                                                  0, 0,
                                                  2, 0,
                                                  3, 0,
                                                  3, 0,
                                                  4, 0)):
            game_map = factory.create(conf)

        self.assertIsInMap(game_map, TreasureField, conf.treasures)
        self.assertIsInMap(game_map, BotField, conf.bots)
        self.assertIsInMap(game_map, BlockField, conf.blocks)
        self.assertIsInMap(
            game_map,
            EmptyField,
            game_map.width * game_map.height - conf.bots - conf.treasures - conf.blocks
        )

    def test_invalid_map(self):
        factory = MapFactory
        with self.assertRaises(ConfigurationError):
            factory.create(CustomConfiguration(bots=2, treasures=2, map_width=3, map_height=1, blocks=0))

        with self.assertRaises(ConfigurationError):
            factory.create(
                CustomConfiguration(map_width=10, map_height=10, blocks=1, bots=1, treasures=1, laser_game=True,
                                    battery_game=False))


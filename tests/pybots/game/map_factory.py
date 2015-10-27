from unittest.mock import patch

from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map_factory import MapFactory
from tests.pybots_test_case import TestCase


class TestMapFactory(TestCase):
    def test_create_basic(self):
        factory = MapFactory()
        game_map = factory.create()

        self.assertIsInMap(game_map, TreasureField)
        self.assertIsInMap(game_map, BotField, MapFactory.BOTS)
        self.assertIsInMap(
            game_map,
            EmptyField,
            game_map.width * game_map.height - MapFactory.BOTS - MapFactory.TREASURES - MapFactory.BLOCKS
        )

    def test_create_small_map(self):
        factory = MapFactory(width=4, height=1, bots=2, treasures=2, blocks=0)

        with patch('random.randint', side_effect=(0, 0,
                                                  0, 0,
                                                  1, 0,
                                                  0, 0,
                                                  2, 0,
                                                  3, 0)):
            game_map = factory.create()

        self.assertIsInMap(game_map, TreasureField, factory.treasures)
        self.assertIsInMap(game_map, BotField, factory.bots)
        self.assertIsInMap(
            game_map,
            EmptyField,
            game_map.width * game_map.height - factory.bots - factory.treasures
        )

    def test_invalid_map(self):
        factory = MapFactory(bots=2, treasures=2, width=3, height=1)
        with self.assertRaises(Exception):
            factory.create()


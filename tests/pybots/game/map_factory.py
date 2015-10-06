from pybots.game.fields.empty_field import EmptyField

from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map_factory import MapFactory
from tests.pybots.pybots_test_case import TestCase


class TestMapFactory(TestCase):
    def test_create_basic(self):
        factory = MapFactory()
        game_map = factory.create()

        self.assertIsInMap(game_map, TreasureField)
        self.assertIsInMap(game_map, BotField, 2)
        self.assertIsInMap(
            game_map,
            EmptyField,
            game_map.width * game_map.height - 3
        )

    def test_create_small_map(self):
        factory = MapFactory(width=3, height=1)
        game_map = factory.create()

        self.assertIsInMap(game_map, TreasureField)
        self.assertIsInMap(game_map, BotField, 2)
        self.assertIsInMap(
            game_map,
            EmptyField,
            game_map.width * game_map.height - 3
        )
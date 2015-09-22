from unittest.case import TestCase

from pybots.game.fields.fields import Fields
from pybots.game.fields.treasure_field import TreasureField


class TestTreasureField(TestCase):
    def test_init(self):
        with self.assertRaises(AssertionError):
            TreasureField(0.1)
        treasure = TreasureField()
        self.assertEqual(treasure.price, treasure.DEFAULT_TREASURE_PRICE, 'Default treasure price with empty init')
        treasure = TreasureField(2)
        self.assertEqual(treasure.price, 2, 'Default treasure price with given price')

    def test_export(self):
        treasure = TreasureField()
        self.assertEqual(treasure.export(), Fields.TREASURE.value, 'Treasure field export')

from unittest.case import TestCase

from pybots.game.fields.fields import Fields
from pybots.game.fields.player_field import PlayerField
from pybots.game.orientations import Orientation


class TestPlayerField(TestCase):
    def test_init(self):
        player = PlayerField(Orientation.NORTH)
        self.assertEqual(player.orientation, Orientation.NORTH, 'Player has to save orientation.')

    def test_export(self):
        player = PlayerField(Orientation.NORTH)
        self.assertEqual(player.export(), Fields.PLAYER.value, 'Player field export')
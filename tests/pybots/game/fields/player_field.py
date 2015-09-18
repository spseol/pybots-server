from unittest.case import TestCase

from pybots.game.fields.fields import Fields
from pybots.game.fields.player_field import PlayerField


class TestPlayerField(TestCase):
    def test_init(self):
        player = PlayerField(0)
        self.assertEqual(player.orientation, 0, 'Player has to save orientation.')

    def test_export(self):
        player = PlayerField(0)
        self.assertEqual(player.export(), Fields.PLAYER, 'Player field export')
from unittest.case import TestCase

from pybots.game.fields.player_field import PlayerField


class TestPlayerField(TestCase):
    def test_init(self):
        player = PlayerField(0)
        self.assertEqual(player.orientation, 0, 'Player has to save orientation.')
import unittest

from pybots.game.map import Map, OutOfMapError


class TestMap(unittest.TestCase):
    def test_getitem(self):
        game_map = Map(1, 1)
        with self.assertRaises(AssertionError):
            game_map[0]
        with self.assertRaises(AssertionError):
            game_map[0, 0, 0]

        with self.assertRaises(OutOfMapError):
            game_map[0, 1]
        with self.assertRaises(OutOfMapError):
            game_map[1, 0]

        self.assertIsNone(game_map[0, 0], 'empty map')
        
    def test_export_map(self):
        game_map = Map(1, 1)
        self.assertEqual(
            game_map.export_map(), 
            [[None]]
        )

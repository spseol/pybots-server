import unittest

from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.fields import Fields
from pybots.game.map import Map, OutOfMapError, UnknownFieldError


class TestMap(unittest.TestCase):
    def test_init(self):
        with self.assertRaises(AssertionError):
            Map(width=0)
        with self.assertRaises(AssertionError):
            Map(height=0)
        with self.assertRaises(AssertionError):
            Map(width=.5)
        with self.assertRaises(AssertionError):
            Map(height=.5)
        with self.assertRaises(AssertionError):
            Map(default_field=None)

    def test_getitem(self):
        game_map = Map(1, 1)
        self.assertIsInstance(game_map[0, 0], EmptyField, 'empty map')

    def test_setitem(self):
        game_map = Map(1, 1)
        field = EmptyField()
        game_map[0, 0] = field
        self.assertIs(game_map[0, 0], field, 'empty map')
        self.assertIsInstance(game_map[0, 0], EmptyField, 'empty map')
        with self.assertRaises(UnknownFieldError):
            game_map[0, 0] = None

    def test__get(self):
        game_map = Map(1, 1)
        with self.assertRaises(AssertionError):
            game_map[0]
        with self.assertRaises(AssertionError):
            game_map[0, 0, 0]

        with self.assertRaises(OutOfMapError):
            game_map[0, 1]
        with self.assertRaises(OutOfMapError):
            game_map[0, 1]

        with self.assertRaises(TypeError):
            game_map[0.1, 0.1]

        with self.assertRaises(OutOfMapError):
            game_map[-1, -1]

    def test_export_map(self):
        game_map = Map(1, 1)
        self.assertEqual(
            game_map.export(),
            [[Fields.EMPTY.value]]
        )

    def test__export_field(self):
        game_map = Map(1, 1)
        getattr(game_map, '_{}__map'.format(game_map.__class__.__name__))[0][0] = None
        with self.assertRaises(UnknownFieldError):
            game_map._export_field(game_map[0, 0])

    def test_resolutions(self):
        game_map = Map(10, 20)
        self.assertEqual(game_map.width, 10, 'Map width')
        self.assertEqual(game_map.height, 20, 'Map height')
from _collections_abc import Iterator
import unittest

from pybots.game.fields.bot_field import BotField
from pybots.game.fields.empty_field import EmptyField
from pybots.game.field import Field
from pybots.game.map import Map, OutOfMapError, UnknownFieldError
from pybots.game.orientations import Orientation


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
            [[Field.EMPTY]]
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
        self.assertIsInstance(game_map.map, list, 'Map property')

    def test_get_next_field(self):
        game_map = Map(2, 1)
        bot = BotField()
        game_map[1, 0] = bot
        self.assertIs(
            game_map.get_next_field((0, 0), Orientation.EAST),
            bot
        )
        self.assertIsNone(
            game_map.get_next_field((0, 0), Orientation.NORTH)
        )

    def test_map_iterator(self):
        game_map = Map(1, 1)
        self.assertIsInstance(iter(game_map), Iterator)
        self.assertEqual(len(list(iter(game_map))), 1)
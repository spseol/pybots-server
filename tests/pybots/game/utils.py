from pybots.game.actions import Action
from pybots.game.map import Map
from pybots.game.orientations import Orientation
from pybots.game.utils import Exportable, get_next_position, get_next_orientation, get_positions_in_row
from tests.test_case import TestCase


class TestGameUtils(TestCase):
    def test_exportable(self):
        with self.assertRaises(TypeError):
            Exportable()

        Exportable.export(Exportable)

    def test_get_next_position(self):
        with self.assertRaises(AssertionError):
            get_next_position((0, ), Orientation(Orientation.NORTH))

        with self.assertRaises(AssertionError):
            get_next_position((0, 0), 0)

        position = 0, 0
        self.assertEqual(get_next_position(position, Orientation.NORTH), (0, -1), 'Next position to NORTH.')
        self.assertEqual(get_next_position(position, Orientation.EAST), (1, 0), 'Next position to EAST.')
        self.assertEqual(get_next_position(position, Orientation.SOUTH), (0, 1), 'Next position to SOUTH.')
        self.assertEqual(get_next_position(position, Orientation.WEST), (-1, 0), 'Next position to WEST.')

    def test_get_next_orientation(self):
        with self.assertRaises(AssertionError):
            get_next_orientation(0, Action.STEP)

        with self.assertRaises(AssertionError):
            get_next_orientation(Orientation.NORTH, 0)

        self.assertEqual(get_next_orientation(Orientation.NORTH, Action.TURN_RIGHT), Orientation.EAST)
        self.assertEqual(get_next_orientation(Orientation.NORTH, Action.TURN_LEFT), Orientation.WEST)

    def test_get_positions_in_row(self):
        game_map = Map(width=3, height=3)

        with self.assertRaises(AssertionError):
            next(get_positions_in_row(None, (0, 0), Orientation.WEST))

        with self.assertRaises(AssertionError):
            next(get_positions_in_row(game_map, None, Orientation.WEST))

        with self.assertRaises(AssertionError):
            next(get_positions_in_row(game_map, (0, 0), None))

        with self.assertRaises(AssertionError):
            next(get_positions_in_row(game_map, (0, 0), Orientation.WEST, limit='foobar'))

        self.assertEqual(
            tuple(get_positions_in_row(game_map, (0, 0), Orientation.SOUTH)),
            (
                (0, 1),
                (0, 2)
            )
        )

        self.assertEqual(
            tuple(get_positions_in_row(game_map, (0, 0), Orientation.WEST)),
            ()
        )

        self.assertEqual(
            tuple(get_positions_in_row(game_map, (0, 0), Orientation.SOUTH, limit=1)),
            (
                (0, 1),
            )
        )

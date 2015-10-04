from pybots.game.actions import Action
from pybots.game.orientations import Orientation
from pybots.game.utils import Exportable, get_next_position, get_next_orientation
from tests.pybots.pybots_test_case import TestCase


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
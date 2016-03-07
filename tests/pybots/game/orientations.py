from pybots.game.orientations import Orientation
from tests.test_case import TestCase


class TestOrientations(TestCase):
    def test_is_horizontal(self):
        orientation_1 = Orientation.EAST
        orientation_2 = Orientation.WEST

        self.assertTrue(orientation_1.is_horizontal, 'East is horizontal orientation.')
        self.assertTrue(orientation_2.is_horizontal, 'West is horizontal orientation.')
        self.assertFalse(orientation_2.is_vertical, 'West is not vertical orientation.')
        self.assertFalse(Orientation.SOUTH.is_horizontal, 'West is not horizontal orientation.')
        self.assertFalse(Orientation.NORTH.is_horizontal, 'North is not horizontal orientation.')

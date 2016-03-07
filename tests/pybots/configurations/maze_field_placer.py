from itertools import permutations

from pybots.configurations import ConfigurationError
from pybots.configurations.maze_field_placer import MazeFieldPlacerMixin
from pybots.game.fields.block_field import BlockField
from pybots.game.map import Map
from tests.test_case import TestCase


class TestMazeFieldPlacer(TestCase):
    def test_random_conf(self):
        game_map = Map(10, 10)

        maze_field_placer = MazeFieldPlacerMixin()
        maze_field_placer.place_blocks(game_map, count=1000)

        positions = set()
        for x, y in permutations(range(1, 9, 2), 2):
            positions.add((x, y))
            positions.add((y, x))

        for position in positions:
            self.assertIsInstance(
                game_map[position],
                BlockField
            )

    def test_check_place_args(self):
        with self.assertRaises(ConfigurationError):
            MazeFieldPlacerMixin._check_place_args(None, None, None)

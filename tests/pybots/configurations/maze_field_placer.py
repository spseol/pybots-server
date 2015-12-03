from pybots.configurations.maze_field_placer import MazeFieldPlacerMixin
from pybots.game.map import Map
from tests.test_case import TestCase


class TestMazeFieldPlacer(TestCase):
    def test_random_conf(self):
        game_map = Map(10, 10)

        maze_field_placer = MazeFieldPlacerMixin()
        maze_field_placer.place_blocks(game_map, count=1000)

        # TODO: tests for maze field placer

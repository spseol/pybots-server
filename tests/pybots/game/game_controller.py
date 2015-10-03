from random import randint

from pybots.game.game import Game
from pybots.game.game_controller import GameController
from tests.pybots.pybots_test_case import TestCase


class TestGameController(TestCase):
    def test_get(self):
        player_id = randint(0, 10 ** 12)

        game = GameController.get(player_id)
        self.assertIsInstance(
            game,
            Game,
            'GameController.get returns Game instance.'
        )

        self.assertIs(
            game,
            GameController.get(player_id),
            'Twice calling of GameController.get returns the same game.'
        )
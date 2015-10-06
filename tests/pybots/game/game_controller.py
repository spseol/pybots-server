from random import randint

from pybots.game.actions import Action
from pybots.game.game import Game, MovementError
from pybots.game.game_controller import game_controller
from tests.pybots.pybots_test_case import TestCase


class TestGameController(TestCase):
    def test_get(self):
        player_id = randint(0, 10 ** 12)

        game = game_controller.get(player_id)
        self.assertIsInstance(
            game,
            Game,
            'GameController.get returns Game instance.'
        )

        self.assertIs(
            game,
            game_controller.get(player_id),
            'Twice calling of GameController.get returns the same game.'
        )

    def test_action_simple(self):
        player_id = 'fake_player_0'

        with self.assertRaises(MovementError):
            for _ in range(game_controller.get(player_id).map.height):
                game_controller.action(player_id, Action.STEP)

        player_id = 'fake_player_1'
        with self.assertRaises(MovementError):
            game_controller.action(player_id, Action.TURN_LEFT)
            for _ in range(game_controller.get(player_id).map.width):
                game_controller.action(player_id, Action.STEP)
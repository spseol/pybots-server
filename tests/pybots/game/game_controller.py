from random import randint

from pybots.game.actions import Action
from pybots.game.game import Game, MovementError
from pybots.game.game_controller import game_controller, GameController
from tests.pybots.pybots_test_case import TestCase


class TestGameController(TestCase):
    def test_get(self):
        bot_id = randint(0, 10 ** 12)

        game = game_controller.get(bot_id)
        self.assertIsInstance(
            game,
            Game,
            'GameController.get returns Game instance.'
        )

        self.assertIs(
            game,
            game_controller.get(bot_id),
            'Twice calling of GameController.get returns the same game.'
        )

    def test_action_simple(self):
        controller = GameController(map_factory_options=dict(height=2, width=2, treasures=0))
        bot_id = 'fake_bot_0'
        with self.assertRaises(MovementError):
            for _ in range(controller.get(bot_id).map.height):
                controller.action(bot_id, Action.STEP)

        bot_id = 'fake_bot_1'
        with self.assertRaises(MovementError):
            controller.action(bot_id, Action.TURN_LEFT)
            for _ in range(controller.get(bot_id).map.width):
                controller.action(bot_id, Action.STEP)
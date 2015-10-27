from random import randint

from pybots.game.actions import Action
from pybots.game.game import Game, MovementError, GameFinished
from pybots.game.game_controller import game_controller, GameController
from tests.pybots_test_case import TestCase


class TestGameController(TestCase):
    def test_get(self):
        bot_id_1 = randint(0, 10 ** 12)
        bot_id_2 = randint(0, 10 ** 12)
        bot_id_3 = randint(0, 10 ** 12)

        game_1 = game_controller.get(bot_id_1)
        self.assertIsInstance(
            game_1,
            Game,
            'GameController.get returns Game instance.'
        )

        self.assertIs(
            game_1,
            game_controller.get(bot_id_1),
            'Twice calling of GameController.get returns the same game.'
        )

        game_2 = game_controller.get(bot_id_2)
        self.assertIs(
            game_1,
            game_2,
            'Two bots in same game.'
        )

        game_3 = game_controller.get(bot_id_3)
        self.assertIsNot(
            game_1,
            game_3,
            'Third bot in new map.'
        )

    def test_action_simple(self):
        controller = GameController(map_factory_options=dict(height=2, width=2, treasures=0, blocks=0))
        bot_id = 0
        with self.assertRaises(MovementError):
            for _ in range(controller.get(bot_id).map.height):
                controller.action(bot_id, Action.STEP)

        bot_id = 1
        with self.assertRaises(MovementError):
            controller.action(bot_id, Action.TURN_LEFT)
            for _ in range(controller.get(bot_id).map.width):
                controller.action(bot_id, Action.STEP)

    def test_finish_game(self):
        controller = GameController(map_factory_options=dict(height=2, width=1, treasures=1, bots=1, blocks=0))
        bot_id = 0
        with self.assertRaises(GameFinished):
            try:
                controller.action(bot_id, Action.STEP)
            except MovementError:
                pass

            controller.action(bot_id, Action.TURN_RIGHT)
            controller.action(bot_id, Action.TURN_RIGHT)
            controller.action(bot_id, Action.STEP)
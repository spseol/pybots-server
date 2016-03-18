from collections import OrderedDict
from random import randint

from pybots.configurations.configuration_provider import ConfigurationProvider
from pybots.configurations.custom_configuration import CustomConfiguration
from pybots.game.actions import Action
from pybots.game.game import Game
from pybots.game.game_controller import GameController
from pybots.game.utils import MovementError, GameFinished
from tests.test_case import TestCase


class TestGameController(TestCase):
    def test_get(self):
        bot_id_1 = randint(0, 10 ** 12)
        bot_id_2 = randint(0, 10 ** 12)
        bot_id_3 = randint(0, 10 ** 12)

        conf_provider = ConfigurationProvider()
        game_controller = GameController(conf_provider)

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
        provider = ConfigurationProvider()
        provider.actual = CustomConfiguration(map_height=2, map_width=2, treasures=0, blocks=0, bots=1)
        controller = GameController(provider)
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
        provider = ConfigurationProvider()
        provider.actual = CustomConfiguration(map_height=2, map_width=1, treasures=1, bots=1, blocks=0)
        controller = GameController(provider)
        bot_id = 0
        with self.assertRaises(GameFinished):
            try:
                controller.action(bot_id, Action.STEP)
            except MovementError:
                pass

            controller.action(bot_id, Action.TURN_RIGHT)
            controller.action(bot_id, Action.TURN_RIGHT)
            controller.action(bot_id, Action.STEP)

    def test_sorted_games(self):
        bot_id_1 = randint(0, 10 ** 12)
        bot_id_2 = randint(0, 10 ** 12)

        game_controller = GameController()

        game_1 = game_controller.get(bot_id_1)
        game_2 = game_controller.get(bot_id_2)

        sorted_games = game_controller.sorted_games()
        self.assertIsInstance(sorted_games, OrderedDict)
        self.assertEqual(len(sorted_games), 2)

        self.assertListEqual(
            [game_2, game_1],
            list(sorted_games.values())
        )


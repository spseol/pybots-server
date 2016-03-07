from datetime import datetime

from pybots.configurations.base_configuration import BaseConfiguration
from pybots.configurations.default_configuration import DefaultConfiguration
from pybots.configurations.custom_configuration import CustomConfiguration
from pybots.configurations.random_field_placer import RandomFieldPlacerMixin
from pybots.game.actions import Action
from pybots.game.fields.block_field import BlockField
from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.game import Game, MovementError, GameFinished, NoFreeBots, BotNotOnTurn
from pybots.game.map import Map
from pybots.game.map_factory import MapFactory
from pybots.game.orientations import Orientation
from tests.test_case import TestCase


class TestGame(TestCase):
    def test_export(self):
        game_map = MapFactory().create(DefaultConfiguration())
        game = Game(game_map)
        bot_id = 0
        game.add_bot(bot_id)

        self.assertCountEqual(
            game.export(bot_id),
            dict(
                map=game_map.export(),
                map_resolutions=(game_map.width, game_map.height)
            )
        )

    def test_not_free_bots(self):
        game_map = MapFactory().create(CustomConfiguration(map_width=2, map_height=1, bots=0, treasures=0, blocks=0))
        game = Game(game_map)
        with self.assertRaises(NoFreeBots):
            game.action('bot_id', Action.STEP)
        self.assertTrue(game.is_filled, 'Game is filled.')

    def test_action_simple_movements(self):
        game_map = Map(width=1, height=1)
        fake_map = [
            [BotField(Orientation.EAST), EmptyField()],
            [EmptyField(), EmptyField()],
        ]
        setattr(game_map, '_{}__map'.format(game_map.__class__.__name__), fake_map)
        game = Game(game_map)
        game._empty_bots_positions = game._map.get_field_occurrences(BotField)

        self.assertFalse(game.is_filled, 'Game has free bot field.')

        fake_bot_id = 'fake_bot_id'

        game.action(fake_bot_id, Action.TURN_RIGHT)
        self.assertEqual(
            game._map[game._bots_positions[fake_bot_id]].orientation,
            Orientation.SOUTH
        )

        game.action(fake_bot_id, Action.TURN_LEFT)
        self.assertEqual(
            game.map[game._bots_positions[fake_bot_id]].orientation,
            Orientation.EAST
        )

        game.action(fake_bot_id, Action.STEP)
        self.assertEqual(
            game._bots_positions[fake_bot_id],
            (1, 0)
        )

        with self.assertRaises(MovementError):
            game.action(fake_bot_id, Action.STEP)
        self.assertEqual(
            game._bots_positions[fake_bot_id],
            (1, 0)
        )

        game.action(fake_bot_id, Action.TURN_RIGHT)

        game.action(fake_bot_id, Action.STEP)
        with self.assertRaises(MovementError):
            game.action(fake_bot_id, Action.STEP)

    def test_action_reach_treasure(self):
        game_map = Map(width=1, height=2)
        fake_map = [
            [TreasureField()],
            [BotField(Orientation.NORTH)],
        ]
        setattr(game_map, '_{}__map'.format(game_map.__class__.__name__), fake_map)
        game = Game(game_map)

        with self.assertRaises(GameFinished):
            game.action('bot_id', Action.STEP)

    def test_action_step_on_block(self):
        game_map = Map(width=1, height=2)
        fake_map = [
            [BlockField()],
            [BotField(Orientation.NORTH)],
        ]
        setattr(game_map, '_{}__map'.format(game_map.__class__.__name__), fake_map)
        game = Game(game_map)

        with self.assertRaises(MovementError):
            game.action('bot_id', Action.STEP)

    def test_action_step_on_bot(self):
        game_map = Map(width=1, height=2)
        fake_map = [
            [BotField(Orientation.SOUTH)],
            [BotField(Orientation.NORTH)],
        ]
        setattr(game_map, '_{}__map'.format(game_map.__class__.__name__), fake_map)
        game = Game(game_map)

        with self.assertRaises(MovementError):
            game.action('bot_id', Action.STEP)

    def test_game_time_flags(self):
        dt = datetime.now()
        game = Game(Map(1, 1))

        self.assertAlmostEqual(
            game.created_at.timestamp(),
            dt.timestamp(),
            places=0,
            msg='created game at patched datetime'
        )

    def test_rounded_game(self):
        class Conf(BaseConfiguration, RandomFieldPlacerMixin):
            map_width = 3
            map_height = 1
            bots = 3
            treasures = 0
            blocks = 0
            rounded_game = True

        conf = Conf()
        game = Game(MapFactory().create(conf), configuration=conf)

        my_bot_1 = 1
        my_bot_2 = 2
        my_bot_3 = 3

        game.add_bot(my_bot_1)
        game.add_bot(my_bot_2)

        game.action(my_bot_1, Action.TURN_LEFT)
        game.action(my_bot_2, Action.TURN_LEFT)

        with self.assertRaises(BotNotOnTurn):
            game.action(my_bot_2, Action.TURN_LEFT)

        game.action(my_bot_1, Action.TURN_LEFT)

        with self.assertRaises(BotNotOnTurn):
            game.action(my_bot_1, Action.TURN_LEFT)

        game.add_bot(my_bot_3)
        with self.assertRaises(BotNotOnTurn):
            game.action(my_bot_3, Action.TURN_LEFT)

        game.action(my_bot_2, Action.TURN_LEFT)
        game.action(my_bot_1, Action.TURN_LEFT)
        game.action(my_bot_3, Action.TURN_LEFT)
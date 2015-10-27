from pybots.game.actions import Action
from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.game import Game, MovementError, GameFinished, NoFreeBots
from pybots.game.map import Map
from pybots.game.map_factory import MapFactory
from pybots.game.orientations import Orientation
from tests.pybots_test_case import TestCase


class TestGame(TestCase):
    def test_export(self):
        game_map = MapFactory().create()
        game = Game(game_map)

        self.assertCountEqual(
            game.export(0),
            dict(
                map=game_map.export(),
                bots=game._export_bots(0),
                map_width=game_map.width,
                map_height=game_map.height,
                map_resolutions=(game_map.width, game_map.height)
            )
        )

    def test_not_free_bots(self):
        game_map = MapFactory(bots=0).create()
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
        game._empty_bots_positions = game.map.get_field_occurrences(BotField)

        with self.assertRaises(GameFinished):
            game.action('bot_id', Action.STEP)

    def test_export_bots(self):
        game = Game(MapFactory(width=2, height=1, bots=2, treasures=0, blocks=0).create())
        my_bot_id = 0
        bots_export = game._export_bots(my_bot_id)

        my_bot_on_fist_field = game.get_bot_position(my_bot_id) == (0, 0)
        self.assertListEqual(
            bots_export,
            [
                dict(x=0, y=0, position=(0, 0), orientation=Orientation.NORTH, your_bot=not my_bot_on_fist_field),
                dict(x=1, y=0, position=(1, 0), orientation=Orientation.NORTH, your_bot=my_bot_on_fist_field)
            ]
        )
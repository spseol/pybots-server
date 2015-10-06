from pybots.game.actions import Action
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map import Map, OutOfMapError
from pybots.game.utils import Exportable, get_next_position


class Game(Exportable):
    def __init__(self, game_map):
        assert isinstance(game_map, Map)
        self._map = game_map
        self._empty_bots_positions = self.map.get_field_occurrences(BotField)
        self._bots_positions = {}
        self._actions = {
            Action.STEP: self._action_step,
            Action.TURN_LEFT: self._action_turn_left,
            Action.TURN_RIGHT: self._action_turn_right,
        }

    @property
    def map(self):
        return self._map

    def action(self, bot_id, action):
        assert isinstance(action, Action)
        if bot_id not in self._bots_positions and self._empty_bots_positions:
            self._bots_positions[bot_id] = self._empty_bots_positions.pop()
        elif bot_id not in self._bots_positions and not self._empty_bots_positions:
            raise NoFreeBots

        action_func = self._actions[action]
        action_func(**dict(bot_id=bot_id))

    def _action_step(self, bot_id, **kwargs):
        actual_position = self._bots_positions[bot_id]
        actual_field = self._map[actual_position]

        bot_orientation = self.map[actual_position].orientation
        new_position = get_next_position(
            actual_position,
            bot_orientation
        )
        try:
            new_field = self.map[new_position]
        except OutOfMapError:
            raise MovementError('New position is out of map.')

        if isinstance(new_field, TreasureField):
            raise GameFinished

        self._map[new_position], self._map[actual_position] = actual_field, new_field

        self._bots_positions[bot_id] = new_position

    def _action_turn_left(self, bot_id, **kwargs):
        bot_field = self.map[self._bots_positions[bot_id]]
        assert isinstance(bot_field, BotField)
        bot_field.rotate(Action.TURN_LEFT)

    def _action_turn_right(self, bot_id, **kwargs):
        bot_field = self.map[self._bots_positions[bot_id]]
        assert isinstance(bot_field, BotField)
        bot_field.rotate(Action.TURN_RIGHT)

    def export(self):
        return dict(
            map=self._map.export()
        )


class MovementError(Exception):
    pass


class GameFinished(Exception):
    pass


class NoFreeBots(Exception):
    pass

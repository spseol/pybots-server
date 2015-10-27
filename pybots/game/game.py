from pybots.game.actions import Action
from pybots.game.fields.block_field import BlockField
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

    def add_bot(self, bot_id):
        if bot_id not in self._bots_positions and self._empty_bots_positions:
            self._bots_positions[bot_id] = self._empty_bots_positions.pop()
        elif bot_id not in self._bots_positions and not self._empty_bots_positions:
            raise NoFreeBots

    def action(self, bot_id, action):
        assert isinstance(action, Action)

        self.add_bot(bot_id)
        action_func = self._actions[action]
        action_func(**dict(bot_id=bot_id))
        return self

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
        elif isinstance(new_field, BotField):
            raise MovementError('Cannot step on another bot.')
        elif isinstance(new_field, BlockField):
            raise MovementError('Cannot step on block.')

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

    def get_bot_position(self, bot_id):
        return self._bots_positions.get(bot_id)

    @property
    def is_filled(self):
        return not bool(self._empty_bots_positions)

    def export(self, for_bot_id):
        return dict(
            map=self._map.export(),
            map_width=self._map.width,
            map_height=self._map.height,
            map_resolutions=(self._map.width, self._map.height),
            bots=self._export_bots(for_bot_id)
        )

    def _export_bots(self, for_bot_id):
        return [
            dict(
                x=bot_position[0],
                y=bot_position[1],
                position=bot_position,
                orientation=self._map[bot_position].orientation,
                your_bot=for_bot_id == bot_id
            ) for bot_id, bot_position in dict(
                list(self._bots_positions.items()) +
                list((bot_id, position) for bot_id, position in enumerate(self._empty_bots_positions))
            ).items()
        ]


class MovementError(Exception):
    pass


class GameFinished(Exception):
    pass


class NoFreeBots(Exception):
    pass

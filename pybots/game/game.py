from collections import deque
from datetime import datetime

from pybots.configurations.configuration_provider import configuration_provider
from pybots.game.actions import Action
from pybots.game.fields.battery_bot_field import BatteryBotField, CriticalBatteryLevel
from pybots.game.fields.block_field import BlockField
from pybots.game.fields.bot_field import BotField
from pybots.game.fields.treasure_field import TreasureField
from pybots.game.map import Map, OutOfMapError
from pybots.game.utils import Exportable, get_next_position, get_positions_in_row, MovementError, ActionError, \
    GameFinished, NoFreeBots, BotNotOnTurn


class Game(Exportable):
    def __init__(self, game_map, created_at=None, last_modified_at=None, configuration=None):
        assert isinstance(game_map, Map)
        assert isinstance(created_at, (datetime, type(None)))
        assert isinstance(last_modified_at, (datetime, type(None)))

        self._map = game_map
        self._empty_bots_positions = self.map.get_field_occurrences(BotField)
        self._bots_positions = {}
        self._actions = {
            Action.STEP: self._action_step,
            Action.TURN_LEFT: self._action_turn_left,
            Action.TURN_RIGHT: self._action_turn_right,
            Action.WAIT: self._action_wait,
            Action.LASER_BEAM: self._action_laser_beam,
        }

        self._configuration = configuration if configuration else configuration_provider.actual
        self._created_at = created_at if created_at else datetime.now()
        self._last_modified_at = last_modified_at if last_modified_at else datetime.now()

        self._bots_deque = deque(maxlen=len(self._empty_bots_positions))

    def add_bot(self, bot_id):
        if bot_id not in self._bots_positions and self._empty_bots_positions:
            self._bots_positions[bot_id] = self._empty_bots_positions.pop()
            self._bots_deque.append(bot_id)
        elif bot_id not in self._bots_positions and not self._empty_bots_positions:
            raise NoFreeBots('In this map is not any free position for bot.')

    def action(self, bot_id, action):
        assert isinstance(action, Action)

        self.add_bot(bot_id)

        if self._configuration.rounded_game and not self.is_bot_on_turn(bot_id):
            raise BotNotOnTurn('This bot is not on turn.')

        bot_field = self.map[self._bots_positions[bot_id]]
        action_func = self._actions[action]
        action_func(**dict(bot_id=bot_id, bot_field=bot_field, bot_position=self._bots_positions[bot_id]))

        self._bots_deque.rotate(-1)
        self._last_modified_at = datetime.now()
        return self

    def _action_step(self, bot_id, bot_field, **kwargs):
        actual_position = self._bots_positions[bot_id]
        bot_field = self._map[actual_position]

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
            raise GameFinished()
        elif isinstance(new_field, BotField):
            raise MovementError('Cannot step on another bot.')
        elif isinstance(new_field, BlockField):
            raise MovementError('Cannot step on block.')

        if self._configuration.battery_game and isinstance(bot_field, BatteryBotField):
            bot_field.drain()

        self._map[new_position], self._map[actual_position] = bot_field, new_field

        self._bots_positions[bot_id] = new_position

    def _action_turn_left(self, bot_field, **kwargs):
        assert isinstance(bot_field, BotField)
        bot_field.rotate(Action.TURN_LEFT)

    def _action_turn_right(self, bot_field, **kwargs):
        assert isinstance(bot_field, BotField)
        bot_field.rotate(Action.TURN_RIGHT)

    def _action_wait(self, bot_field, **kwargs):
        if not self._configuration.battery_game:
            raise ActionError('This game is not a battery game.')

        assert isinstance(bot_field, BatteryBotField)
        bot_field.charge()

    def _action_laser_beam(self, bot_field, bot_position, **kwargs):
        if not self._configuration.laser_game:
            raise ActionError('This game is not a laser game.')

        assert isinstance(bot_field, BatteryBotField)
        try:
            bot_field.drain(2)  # TODO: as constant
        except CriticalBatteryLevel as e:
            raise MovementError(e)

        for position in get_positions_in_row(self.map, bot_position, bot_field.orientation):
            field = self.map[position]
            if isinstance(field, self._configuration.default_empty_map_field):
                continue
            if isinstance(field, BatteryBotField):
                field.drain()
                break
            if isinstance(field, BlockField):
                self.map[position] = self._configuration.default_empty_map_field()
                break

    def get_bot_position(self, bot_id):
        return self._bots_positions.get(bot_id)

    def is_bot_on_turn(self, bot_id):
        return self._bots_deque and self._bots_deque[0] == bot_id

    @property
    def is_filled(self):
        return not bool(self._empty_bots_positions)

    @property
    def map(self):
        return self._map

    @property
    def created_at(self):
        return self._created_at

    @property
    def last_modified_at(self):
        return self._last_modified_at

    def export(self, for_bot_id):
        game_map_export = self._map.export(for_bot_id=for_bot_id)
        bot_position = self._bots_positions.get(for_bot_id)
        game_map_export[bot_position[1]][bot_position[0]].update(dict(
            your_bot=True
        ))
        return dict(
            map=game_map_export,
            map_resolutions=(self._map.width, self._map.height)
        )

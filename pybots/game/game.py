from pybots.game.actions import Action
from pybots.game.fields.player_field import PlayerField
from pybots.game.map import Map, OutOfMapError
from pybots.game.utils import Exportable, get_next_position


class Game(Exportable):
    def __init__(self, game_map):
        assert isinstance(game_map, Map)
        self._map = game_map
        self._empty_player_positions = self.map.get_field_positions(PlayerField)
        self._players_positions = {}
        self._actions = {
            Action.STEP: self._action_step,
            Action.TURN_LEFT: self._action_turn_left,
            Action.TURN_RIGHT: self._action_turn_right,
        }

    @property
    def map(self):
        return self._map

    def action(self, player_id, action):
        assert isinstance(action, Action)
        if player_id not in self._players_positions:
            self._players_positions[player_id] = self._empty_player_positions.pop()

        action_func = self._actions[action]
        action_func(**dict(player_id=player_id))

    def _action_step(self, player_id, **kwargs):
        actual_position = self._players_positions[player_id]
        orientation = self.map[actual_position].orientation
        new_position = get_next_position(
            actual_position,
            orientation
        )
        try:
            self.map[new_position]
        except OutOfMapError:
            raise MovementError('New position is out of map.')

        actual_field = self._map[actual_position]
        new_field = self._map[new_position]

        self._map[new_position], self._map[actual_position] = actual_field, new_field

        self._players_positions[player_id] = new_position

    def _action_turn_left(self, player_id, **kwargs):
        player_field = self.map[self._players_positions[player_id]]
        assert isinstance(player_field, PlayerField)
        player_field.rotate(Action.TURN_LEFT)

    def _action_turn_right(self, player_id, **kwargs):
        player_field = self.map[self._players_positions[player_id]]
        assert isinstance(player_field, PlayerField)
        player_field.rotate(Action.TURN_RIGHT)

    def export(self):
        return dict(
            map=self._map.export()
        )


class MovementError(Exception):
    pass

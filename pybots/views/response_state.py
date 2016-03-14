from enum import Enum

from flask.json import jsonify


class ResponseState(Enum):
    GAME_WON = 'game_won', 200
    GAME_LOST = 'game_lost', 200

    UNKNOWN_BOT = 'unknown_bot', 404  # given bot_id is unknown
    INVALID_ACTION = 'invalid_action', 404  # given action is unknown
    # TODO: rename action error to better name
    ACTION_ERROR = 'action_error', 404  # action is not OK for this game

    MOVEMENT_ERROR = 'movement_error', 200  # movement into wall or bot is not OK
    MOVEMENT_SUCCESS = 'movement_success', 200  # action was successful
    BOT_NOT_ON_TURN = 'bot_not_on_turn', 200  # this bot is not on turn
    CRITICAL_BATTERY_LEVEL = 'critical_battery_level', 200  # bot has not enough battery level for action

    def __init__(self, state, code=None):
        self.state = state
        self.code = code if code else 200

    def as_response(self, **kwargs):
        kwargs.update({self.__class__.__name__: self.state})
        return jsonify(**kwargs), self.code

    @property
    def response(self):
        return self.as_response()


ResponseState.__name__ = 'state'

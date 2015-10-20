from enum import Enum

from flask.json import jsonify


class ResponseState(Enum):
    GAME_WON = 'game_won', 200
    GAME_LOST = 'game_lost', 200

    UNKNOWN_BOT = 'unknown_bot', 404
    INVALID_ACTION = 'invalid_action', 404

    MOVEMENT_ERROR = 'movement_error', 200
    MOVEMENT_SUCCESS = 'movement_success', 200

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

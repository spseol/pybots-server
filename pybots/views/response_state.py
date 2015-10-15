from enum import Enum

from flask.json import jsonify


class ResponseState(Enum):
    GAME_WON = 'game_won', 200
    GAME_LOST = 'game_lost', 200
    UNKNOWN_BOT = 'unknown_bot', 404
    INVALID_ACTION = 'invalid_action', 404
    MOVEMENT_ERROR = 'movement_error', 404

    def __init__(self, state, code=None):
        self.state = state
        self.code = code if code else 200

    @property
    def response(self):
        return jsonify(**{self.__class__.__name__: self.state}), self.code


ResponseState.__name__ = 'state'

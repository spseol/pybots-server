from flask.json import jsonify
from flask.views import MethodView

from pybots.game.game import Game
from pybots.game.game_controller import game_controller
from pybots.views.response_state import ResponseState
from pybots.views.utils import args_to_kwargs


class GameView(MethodView):
    decorators = [args_to_kwargs]

    def get(self, bot_id=None, *args, **kwargs):
        if bot_id not in game_controller.games:
            return ResponseState.UNKNOWN_BOT.response

        game = game_controller.games.get(bot_id, None)

        assert isinstance(game, Game)
        return jsonify(game.export())

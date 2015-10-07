from pprint import pformat

from flask.json import jsonify
from flask.views import MethodView

from pybots.game.game import Game
from pybots.game.game_controller import game_controller
from pybots.views.utils import args_to_kwargs


class GameView(MethodView):
    decorators = [args_to_kwargs]

    def get(self, user_id=None, *args, **kwargs):
        if not user_id:
            return 'Invalid request', 404

        if user_id not in game_controller.games:
            return 'Unknown user_id', 404

        game = game_controller.games.get(user_id, None)

        assert isinstance(game, Game)
        return jsonify(game.export())

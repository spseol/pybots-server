from pprint import pformat

from flask.views import MethodView

from pybots.game.game import Game
from pybots.game.game_controller import GameController
from pybots.views.utils import args_to_kwargs


class GameView(MethodView):
    decorators = [args_to_kwargs]

    def get(self, user_id=None, *args, **kwargs):
        if not user_id:
            return 'Invalid request', 404

        if user_id not in GameController.games:
            return 'Unknown user_id', 404

        game = GameController.games.get(user_id, None)

        assert isinstance(game, Game)
        return pformat(game.export())

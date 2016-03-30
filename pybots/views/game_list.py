from operator import itemgetter

from flask.json import jsonify
from flask.views import MethodView
from pybots.game.game_controller import game_controller


class GameListView(MethodView):
    def get(self):
        return jsonify(dict(
            games=list(dict(bot_id=bot_id, last_modified=game.last_modified_at.timestamp())
                       for bot_id, game in sorted(game_controller.games.items(), key=lambda t: itemgetter(1)(t).last_modified_at))
        )), 200

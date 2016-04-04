from operator import attrgetter

from flask.json import jsonify
from flask.views import MethodView
from pybots.game.game_controller import game_controller


class GameListView(MethodView):
    def get(self):
        reversed_games = {val: key for key, val in game_controller.games.items()}
        return jsonify(dict(
            games=list(
                dict(
                    bot_id=reversed_games.get(game),
                    last_modified=game.last_modified_at.timestamp()
                ) for game in sorted(
                    set(game_controller.games.values()),
                    key=attrgetter('last_modified_at')
                )
            )
        )), 200

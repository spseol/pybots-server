from flask.json import jsonify
from flask.views import MethodView
from flask import request

from pybots.game.game_controller import game_controller


class IndexView(MethodView):
    def get(self, *args, **kwargs):
        headers = sorted(request.headers.items())
        # headers.append(time())
        bot_id = abs(hash(
            tuple(headers)
        ))

        game_controller.get(bot_id)
        return jsonify(id=bot_id, bot_id=bot_id)

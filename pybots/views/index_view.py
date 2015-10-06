from flask.json import jsonify
from flask.views import View
from flask import request

from pybots.game.game_controller import game_controller


class IndexView(View):
    def dispatch_request(self, *args, **kwargs):
        headers = sorted(request.headers.items())
        # headers.append(time())
        client_id = hash(
            tuple(headers)
        )

        game_controller.get(client_id)
        return jsonify(id=client_id)

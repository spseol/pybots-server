from uuid import uuid4

from flask.json import jsonify

from flask.views import MethodView

from pybots.game.game_controller import game_controller


class IndexView(MethodView):
    def get(self, *args, **kwargs):
        bot_id = uuid4().int

        game_controller.get(bot_id)
        return jsonify(bot_id=bot_id)

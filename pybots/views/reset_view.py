from flask import jsonify

from flask.views import MethodView

from pybots.configurations.configuration_provider import configuration_provider
from pybots.game.game_controller import game_controller


class ResetView(MethodView):
    def post(self):
        game_controller.games = {}
        configuration_provider._actual = None

        return jsonify(state='reset_success'), 200  # TODO: as response state

from flask import jsonify
from flask.views import MethodView

from pybots.game.actions import Action
from pybots.game.game_controller import GameController
from pybots.views.utils import form_to_kwargs, args_to_kwargs


class ActionView(MethodView):
    decorators = [form_to_kwargs, args_to_kwargs]

    def post(self, player_id=None, action=None, *args, **kwargs):
        if not all((player_id, action)):
            return 'Invalid request', 404

        GameController.action(
            player_id,
            Action(int(action))
        )

        return jsonify(**GameController.get(player_id).export()), 200

from flask import jsonify
from flask.views import MethodView

from pybots.game.actions import Action
from pybots.game.game import NoFreeBots, MovementError
from pybots.game.game_controller import game_controller
from pybots.views.utils import form_to_kwargs


class ActionView(MethodView):
    decorators = [form_to_kwargs]

    def post(self, bot_id=None, action=None, *args, **kwargs):
        if not all((bot_id, action, isinstance(bot_id, int))):
            return 'Invalid request', 404
        try:
            game_controller.action(
                bot_id,
                Action(int(action))
            )
        except NoFreeBots:
            return jsonify(state='Game finished!')
        except MovementError:
            return jsonify(state='Movement error!')

        return jsonify(**game_controller.get(bot_id).export()), 200

from flask.views import MethodView

from pybots.game.actions import Action
from pybots.game.game import NoFreeBots, MovementError, GameFinished, BotNotOnTurn
from pybots.game.game_controller import game_controller
from pybots.views.response_state import ResponseState
from pybots.views.utils import form_to_kwargs


class ActionView(MethodView):
    decorators = [form_to_kwargs]

    def post(self, bot_id=None, action=None, *args, **kwargs):
        try:
            bot_id = int(bot_id)
        except (ValueError, TypeError):
            return ResponseState.UNKNOWN_BOT.response

        if bot_id not in game_controller.games:
            return ResponseState.UNKNOWN_BOT.response

        try:
            action = Action(action)
        except (ValueError, TypeError):
            return ResponseState.INVALID_ACTION.response

        try:
            game = game_controller.action(
                bot_id,
                action
            )
            return ResponseState.MOVEMENT_SUCCESS.as_response(game=game.export(bot_id))
        except NoFreeBots:
            # TODO: is it special state?
            pass
        except BotNotOnTurn:
            return ResponseState.BOT_NOT_ON_TURN.response
        except MovementError:
            return ResponseState.MOVEMENT_ERROR.response
        except GameFinished:
            return ResponseState.GAME_WON.response

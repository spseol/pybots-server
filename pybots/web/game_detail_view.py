from datetime import datetime

from flask.helpers import url_for
from flask.templating import render_template
from flask.views import MethodView
from werkzeug.utils import redirect

from pybots.game.game_controller import game_controller
from pybots.views.utils import args_to_kwargs


class GameDetailView(MethodView):
    decorators = [args_to_kwargs]

    TIMEOUT_DELETE = 60

    def get(self, bot_id=None, **kwargs):
        game = game_controller.games.get(bot_id)
        if not game:
            return 'Game not found.', 404
        return render_template('detail.html', game=game, bot_id=bot_id)

    def post(self, bot_id=None, **kwargs):
        if bot_id:
            game = game_controller.games.get(bot_id)
            if not game:
                return 'Game not found.', 404
            if game.last_modified_at.timestamp() + self.TIMEOUT_DELETE > datetime.now().timestamp():
                return 'Game cannot be deleted', 403
            game_controller.remove_game(game)
        else:
            now_timestamp = datetime.now().timestamp()
            for game in game_controller.games.values():
                if game.last_modified_at.timestamp() + self.TIMEOUT_DELETE < now_timestamp:
                    game_controller.remove_game(game)

        return redirect(url_for('admin_index'))

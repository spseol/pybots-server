from flask.helpers import url_for

from flask.templating import render_template
from flask.views import MethodView
from werkzeug.utils import redirect

from pybots.game.game_controller import game_controller
from pybots.views.utils import args_to_kwargs


class GameView(MethodView):
    decorators = [args_to_kwargs]

    def get(self, bot_id=None, **kwargs):
        game = game_controller.games.get(bot_id)
        if not game:
            return 'Game not found.', 404
        return render_template('detail.html', game=game)

    def post(self, bot_id=None, **kwargs):
        game = game_controller.games.get(bot_id)
        if not game:
            return 'Game not found.', 404
        game_controller.remove_game(game)
        return redirect(url_for('admin_index'))

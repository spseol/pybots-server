from flask.templating import render_template
from flask.views import MethodView

from pybots.game.game_controller import game_controller


class IndexView(MethodView):
    def get(self):
        return render_template('index.html', games=game_controller.games)

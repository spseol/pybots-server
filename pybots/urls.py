from pybots.views.action_view import ActionView
from pybots.views.game_view import GameView
from pybots.views.index_view import IndexView

urls = (
    (u'/', IndexView.as_view('index')),
    (u'/game/<bot_id>', GameView.as_view('game')),
    (u'/action', ActionView.as_view('action')),
)

from pybots.views.game_view import GameView
from pybots.views.index_view import IndexView

urls = (
    (u'/', IndexView.as_view('index')),
    (u'/game/<user_id>', GameView.as_view('game')),
)

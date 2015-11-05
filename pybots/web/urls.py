from pybots.web.detail_view import GameView
from pybots.web.index_view import IndexView

urls = (
    (u'/admin', IndexView.as_view('admin_index')),
    (u'/admin/<int:bot_id>', GameView.as_view('admin_game_detail')),
)

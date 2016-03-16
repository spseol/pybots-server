from pybots.web.game_detail_view import GameDetailView
from pybots.web.admin_index_view import AdminIndexView
from pybots.web.index_view import IndexView

urls = (
    (u'/', IndexView.as_view('index')),
    (u'/admin', AdminIndexView.as_view('admin_index')),
    (u'/admin/<int:bot_id>', GameDetailView.as_view('admin_game_detail')),
    (u'/admin/<int:bot_id>', GameDetailView.as_view('admin_game_delete')),
)

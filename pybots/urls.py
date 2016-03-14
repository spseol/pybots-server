from pybots.views.action_view import ActionView
from pybots.views.game_view import GameView
from pybots.views.index_view import IndexView
from pybots.views.info_view import InfoView
from pybots.views.reset_view import ResetView
from pybots.web.urls import urls as web_urls

urls = (
    (u'/', IndexView.as_view('index')),
    (u'/info', InfoView.as_view('info')),
    (u'/game/<int:bot_id>', GameView.as_view('game')),
    (u'/action', ActionView.as_view('action')),
    (u'/reset', ResetView.as_view('reset')),
)

urls = urls + web_urls

from operator import attrgetter
from collections import OrderedDict

from pybots.configurations.configuration_provider import configuration_provider
from pybots.game.actions import Action
from pybots.game.game import Game
from pybots.game.map_factory import MapFactory
from pybots.game.utils import GameFinished


class GameController(object):
    _map_factory = None

    def __init__(self, conf_provider=configuration_provider):
        self._conf_provider = conf_provider
        self.games = {}

    def get(self, bot_id):
        assert isinstance(bot_id, int)
        game = self.games.get(bot_id, None)
        if game:
            return game

        # try to find game with free bot
        game = self.open_game
        if game:
            game.add_bot(bot_id)
            self.games.update({
                bot_id: game
            })
            return game

        game = Game(MapFactory.create(self._conf_provider.actual))
        game.add_bot(bot_id)
        self.games.update({bot_id: game})
        return game

    @property
    def open_game(self):
        for game in self.sorted_games(reverse=False).values():
            if game.is_filled:
                continue
            return game
        return None

    def action(self, bot_id, action):
        assert action in Action
        game = self.get(bot_id)
        try:
            return game.action(bot_id, action)
        except GameFinished:
            self.remove_game(game)
            raise

    def sorted_games(self, key='last_modified_at', reverse=True):
        return OrderedDict(sorted(self.games.items(), key=lambda x: attrgetter(key)(x[1]), reverse=reverse))

    def remove_game(self, game):
        self.games = {bot_id: g for bot_id, g in self.games.items() if g is not game}


game_controller = GameController()

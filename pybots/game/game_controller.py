from pybots.configurations.configuration_provider import configuration_provider
from pybots.game.actions import Action
from pybots.game.game import Game, GameFinished
from pybots.game.map_factory import MapFactory


class GameController(object):
    _map_factory = None

    def __init__(self, conf_provider=configuration_provider):
        self._map_factory = MapFactory()
        self._conf_provider = conf_provider
        self.games = {}

    def get(self, bot_id):
        assert isinstance(bot_id, int)
        game = self.games.get(bot_id, None)
        if game:
            return game

        # try to find game with free bot
        for game in self.games.values():
            if game.is_filled:
                continue
            game.add_bot(bot_id)
            self.games.update({
                bot_id: game
            })
            return game

        game = Game(self._map_factory.create(self._conf_provider.actual))
        game.add_bot(bot_id)
        self.games.update({bot_id: game})
        return game

    def action(self, bot_id, action):
        assert action in Action
        game = self.get(bot_id)
        try:
            return game.action(bot_id, action)
        except GameFinished:
            self.games = {bot_id: g for bot_id, g in self.games.items() if g is not game}
            raise


game_controller = GameController()

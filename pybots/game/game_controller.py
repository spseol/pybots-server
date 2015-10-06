from pybots.game.actions import Action
from pybots.game.game import Game
from pybots.game.map_factory import MapFactory


class GameController(object):
    games = {}
    _map_factory = None

    def __init__(self, map_factory_options=None):
        if not map_factory_options:
            map_factory_options = {}
        self._map_factory = MapFactory(**map_factory_options)

    def get(self, user_id):
        game = self.games.get(str(user_id), None)
        if not game:
            game_map = self._map_factory.create()
            game = Game(game_map)
            # TODO: ASAP resolve params casting request params
            self.games[str(user_id)] = game
        return game

    def action(self, user_id, action):
        assert action in Action
        game = self.get(user_id)
        game.action(user_id, action)


game_controller = GameController()

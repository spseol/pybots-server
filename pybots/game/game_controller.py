from pybots.game.actions import Action
from pybots.game.game import Game
from pybots.game.map_factory import MapFactory


class GameController(object):
    games = {}
    _map_factory = MapFactory()

    @classmethod
    def get(cls, user_id):
        game = cls.games.get(str(user_id), None)
        if not game:
            game_map = cls._map_factory.create()
            game = Game(game_map)
            # TODO: ASAP resolve params casting request params
            cls.games[str(user_id)] = game
        return game

    @classmethod
    def action(cls, user_id, action):
        assert action in Action
        game = cls.get(user_id)
        game.action(user_id, action)

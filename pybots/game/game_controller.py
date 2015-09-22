from pybots.game.map_factory import MapFactory


class GameController(object):
    maps = {}
    _map_factory = MapFactory()

    @classmethod
    def get(cls, user_id):
        game_map = cls.maps.get(str(user_id), None)
        if not game_map:
            game_map = cls._map_factory.create()
            # TODO: ASAP resolve params casting request params
            cls.maps[str(user_id)] = game_map
        return game_map

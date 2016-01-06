from pybots.configurations.base_configuration import BaseConfiguration
from pybots.game.map import Map


class MapFactory(object):
    def create(self, conf):
        assert isinstance(conf, BaseConfiguration)
        game_map = Map(width=conf.map_width,
                       height=conf.map_height,
                       default_field=conf.default_empty_map_field)

        if game_map.width * game_map.height < sum((conf.bots, conf.treasures, conf.blocks)):
            raise InvalidMapError('Cannot place {} bots, {} treasures and {} blocks into {}x{} map.'
                                  .format(conf.bots, conf.treasures, conf.blocks, game_map.width, game_map.height))

        conf.place_fields(game_map=game_map, conf=conf)
        return game_map


class InvalidMapError(Exception):
    pass

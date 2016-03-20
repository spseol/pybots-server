from names import get_first_name
from pybots.configurations import ConfigurationError

from pybots.configurations.base_configuration import BaseConfiguration
from pybots.game.fields.bot_field import BotField
from pybots.game.map import Map


class MapFactory(object):
    @staticmethod
    def create(conf):
        assert isinstance(conf, BaseConfiguration)
        game_map = Map(width=conf.map_width,
                       height=conf.map_height,
                       default_field=conf.default_empty_map_field)

        if game_map.width * game_map.height < sum((conf.bots, conf.treasures, conf.blocks)):
            raise ConfigurationError('Cannot place {} bots, {} treasures and {} blocks into {}x{} map.'
                                     .format(conf.bots, conf.treasures, conf.blocks, game_map.width, game_map.height))

        if conf.laser_game and not conf.battery_game:
            raise ConfigurationError('Laser game need to enable batteries.')

        conf.place_fields(game_map=game_map, conf=conf)
        MapFactory._provide_names_for_bots(game_map)

        return game_map

    @staticmethod
    def _provide_names_for_bots(game_map):
        assert isinstance(game_map, Map)
        bots_positions = game_map.get_field_occurrences(BotField)
        names = set()
        while len(names) < len(bots_positions):
            names.add(get_first_name('male'))

        for position in bots_positions:
            bot = game_map[position]
            assert isinstance(bot, BotField)
            bot.name = names.pop()

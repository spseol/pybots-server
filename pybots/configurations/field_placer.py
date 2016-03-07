from abc import ABCMeta, abstractmethod

from pybots.configurations import ConfigurationError
from pybots.game.fields.battery_bot_field import BatteryBotField
from pybots.game.fields.bot_field import BotField


class FieldPlacerMixin(object, metaclass=ABCMeta):
    blocks = bots = treasures = None

    @abstractmethod
    def place_bots(self, *args, **kwargs):
        return

    @abstractmethod
    def place_blocks(self, *args, **kwargs):
        return

    @abstractmethod
    def place_treasures(self, *args, **kwargs):
        return

    def place_fields(self, game_map=None, *args, **kwargs):
        bot_field_class = BatteryBotField if getattr(kwargs.get('conf', None), 'battery_game', None) else BotField
        self.place_blocks(game_map=game_map, count=self.blocks, *args, **kwargs)
        self.place_bots(game_map=game_map, count=self.bots, field_class=bot_field_class, *args, **kwargs)
        self.place_treasures(game_map=game_map, count=self.treasures, *args, **kwargs)

    @classmethod
    def _check_place_args(cls, game_map, count, field_class):
        if game_map is None or count is None or field_class is None:
            raise ConfigurationError('Given parameters for placing methods is not valid.')

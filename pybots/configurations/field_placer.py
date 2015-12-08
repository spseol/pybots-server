from abc import ABCMeta, abstractmethod


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
        self.place_blocks(game_map=game_map, count=self.blocks, *args, **kwargs)
        self.place_bots(game_map=game_map, count=self.bots, *args, **kwargs)
        self.place_treasures(game_map=game_map, count=self.treasures, *args, **kwargs)

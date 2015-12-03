from abc import ABCMeta


class FieldPlacerMixin(object, metaclass=ABCMeta):
    blocks = bots = treasures = None
    place_bots = place_treasures = place_blocks = lambda self, *args, **kwargs: None

    def place_fields(self, game_map=None, *args, **kwargs):
        self.place_blocks(game_map=game_map, count=self.blocks, *args, **kwargs)
        self.place_bots(game_map=game_map, count=self.bots, *args, **kwargs)
        self.place_treasures(game_map=game_map, count=self.treasures, *args, **kwargs)

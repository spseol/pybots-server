from pybots.game.fields.field import Field
from pybots.game.fields.fields import Fields


class PlayerField(Field):
    def __init__(self, orientation):
        self.orientation = orientation

    def export(self):
        # TODO: fix JSON serializing enum
        return Fields.PLAYER.value

from pybots.game.fields.field import Field


class PlayerField(Field):
    def __init__(self, orientation):
        self.orientation = orientation

    def export(self):
        # TODO: specify enumeration with field types
        return 'player'

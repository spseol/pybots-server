from pybots.game.field import Field


class EmptyField(Field):
    def export(self):
        return None
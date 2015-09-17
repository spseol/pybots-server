from pybots.game.fields.field import Field


class EmptyField(Field):
    def export(self):
        return None

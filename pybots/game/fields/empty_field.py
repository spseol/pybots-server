from pybots.game.fields.field import Field
from pybots.game.fields.fields import Fields


class EmptyField(Field):
    def export(self):
        return Fields.EMPTY

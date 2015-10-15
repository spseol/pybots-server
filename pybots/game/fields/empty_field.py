from pybots.game.fields.field import Field
from pybots.game.field import Field as FieldEnum


class EmptyField(Field):
    def export(self):
        return FieldEnum.EMPTY

from pybots.game.field import Field as FieldEnum, FIELD_KEY
from pybots.game.fields.field import Field


class EmptyField(Field):
    def export(self, *args, **kwargs):
        return {
            FIELD_KEY: FieldEnum.EMPTY
        }

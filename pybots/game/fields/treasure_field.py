from pybots.game.field import Field as FieldEnum, FIELD_KEY
from pybots.game.fields.field import Field


class TreasureField(Field):
    DEFAULT_TREASURE_PRICE = 1

    def __init__(self, price=DEFAULT_TREASURE_PRICE):
        assert isinstance(price, int), 'Price has to be int type'
        self.price = price

    def export(self, *args, **kwargs):
        return {
            FIELD_KEY: FieldEnum.TREASURE
        }

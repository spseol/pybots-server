from pybots.game.fields.field import Field
from pybots.game.fields.fields import Fields


class TreasureField(Field):
    DEFAULT_TREASURE_PRICE = 1

    def __init__(self, price=DEFAULT_TREASURE_PRICE):
        assert isinstance(price, int), 'Price has to be int type'
        self.price = price

    def export(self):
        return Fields.TREASURE

import unittest

from pybots.game.field import Field, FIELD_KEY
from pybots.game.fields.empty_field import EmptyField


class TestEmptyField(unittest.TestCase):
    def test_export(self):
        field = EmptyField()
        self.assertEqual(field.export(), {FIELD_KEY: Field.EMPTY})

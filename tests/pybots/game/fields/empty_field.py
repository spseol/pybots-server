import unittest

from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.fields import Fields


class TestEmptyField(unittest.TestCase):
    def test_export(self):
        field = EmptyField()
        self.assertEqual(field.export(), Fields.EMPTY.value)

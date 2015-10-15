import unittest

from pybots.game.fields.empty_field import EmptyField
from pybots.game.field import Field


class TestEmptyField(unittest.TestCase):
    def test_export(self):
        field = EmptyField()
        self.assertEqual(field.export(), Field.EMPTY)

import unittest

from pybots.game.fields.field import Field


class TestField(unittest.TestCase):
    def test_export(self):
        field = Field()
        with self.assertRaises(NotImplementedError):
            field.export()

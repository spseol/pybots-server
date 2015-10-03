import unittest

from pybots.game.fields.field import Field


class TestField(unittest.TestCase):
    def test_export(self):
        with self.assertRaises(TypeError):
            field = Field()

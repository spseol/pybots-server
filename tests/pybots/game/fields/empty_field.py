import unittest

from pybots.game.fields.empty_field import EmptyField


class TestEmptyField(unittest.TestCase):
    def test_export(self):
        field = EmptyField()
        self.assertIsNone(field.export())

import json

from flask.json import loads

from pybots.game.actions import Action

from pybots.json_encoder import JSONEncoder
from tests.pybots_test_case import TestCase


class TestJsonEncoder(TestCase):
    def test_default(self):
        encoder = JSONEncoder()
        assert isinstance(encoder, json.JSONEncoder)

        data = dict(foo=Action.STEP)

        through_json_data = loads(encoder.encode(data))

        self.assertEqual(
            through_json_data.get('foo'),
            Action.STEP.value
        )

        class JSONNotSerializable(object):
            pass

        with self.assertRaises(TypeError):
            encoder.encode(JSONNotSerializable())
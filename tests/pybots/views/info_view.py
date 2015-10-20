from flask.json import loads, dumps
from flask.wrappers import Response

from main import app
from pybots.game.actions import Action
from pybots.game.orientations import Orientation
from pybots.game.field import Field
from pybots.views.response_state import ResponseState
from tests.pybots_test_case import TestCase


class TestInfoView(TestCase):
    def test_get(self):
        with app.test_client() as client:
            response = client.get('/info')
            assert isinstance(response, Response)
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)
            data = loads(response.data)

            self.assertIn(Action.__name__.lower(), data)
            self.assertIn(Orientation.__name__.lower(), data)
            self.assertIn(Field.__name__.lower(), data)
            self.assertIn(ResponseState.__name__.lower(), data)

            self.assertDictEqual(
                data[Orientation.__name__.lower()],
                loads(dumps({str(m.name): str(m.value) for m in Orientation}))
            )
            self.assertDictEqual(
                data[Action.__name__.lower()],
                loads(dumps({str(m.name): str(m.value) for m in Action}))
            )
            self.assertDictEqual(
                data[Field.__name__.lower()],
                loads(dumps({str(m.name): str(m.value) for m in Field}))
            )
            self.assertDictEqual(
                data[ResponseState.__name__.lower()],
                loads(dumps({str(m.name): list(m.value) for m in ResponseState}))
            )

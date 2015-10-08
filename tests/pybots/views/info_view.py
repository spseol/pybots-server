from flask.json import loads, dumps
from flask.wrappers import Response

from main import app
from pybots.game.actions import Action
from pybots.game.orientations import Orientation
from tests.pybots.pybots_test_case import TestCase


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

            self.assertDictEqual(
                data[Orientation.__name__.lower()],
                loads(dumps({str(m.value): str(m.name) for m in Orientation}))
            )
            self.assertDictEqual(
                data[Action.__name__.lower()],
                loads(dumps({m.value: str(m.name) for m in Action}))
            )
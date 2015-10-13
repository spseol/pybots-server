from flask.json import loads
from flask.wrappers import Response

from main import app
from tests.pybots_test_case import TestCase


class TestIndexView(TestCase):
    def test_get(self):
        with app.test_client() as client:
            response = client.get('/')
            assert isinstance(response, Response)
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)
            data = loads(response.data)
            self.assertIn('bot_id', data)

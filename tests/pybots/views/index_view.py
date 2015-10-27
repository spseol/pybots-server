from flask.json import loads
from flask.wrappers import Response

from tests.test_case import TestCase


class TestIndexView(TestCase):
    def test_get(self):
        with self.test_client as client:
            response = client.get('/')
            assert isinstance(response, Response)
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)
            data = loads(response.data)
            self.assertIn('bot_id', data)
            first_bot_id = data.get('bot_id')

            response = client.get('/')
            assert isinstance(response, Response)
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)
            data = loads(response.data)
            self.assertIn('bot_id', data)
            second_bot_id = data.get('bot_id')

            self.assertNotEqual(
                first_bot_id,
                second_bot_id,
                'Two requests to index views return new bot identifiers.'
            )


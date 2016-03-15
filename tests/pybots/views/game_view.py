from random import randint

from flask.json import loads
from flask.wrappers import Response
from tests.test_case import TestCase


class TestGameView(TestCase):
    def test_invalid_request(self):
        with self.test_client as client:
            response = client.get('/game')
            assert isinstance(response, Response)
            self.assertEqual(response.status_code, 404)

            response = client.get('/game/{}'.format(randint(1, 10 ** 9)))
            self.assertEqual(response.status_code, 404, 'Request to unknown game.')

    def test_valid_request(self):
        with self.test_client as client:
            bot_id = loads(client.get('/').data).get('bot_id')
            response = client.get('/game/{}'.format(bot_id))
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)
            data = loads(response.data)
            self.assertIn('map', data)
            self.assertIn('map_info', data)
            map_info = data.get('map_info')
            self.assertIn('map_resolutions', map_info)
            self.assertIn('width', map_info.get('map_resolutions'))
            self.assertIn('height', map_info.get('map_resolutions'))
            self.assertIn('battery_game', map_info)
            self.assertIn('laser_game', map_info)
            self.assertIn('rounded_game', map_info)

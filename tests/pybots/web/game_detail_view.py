from random import randint

from flask.json import loads

from tests.test_case import TestCase


class TestGameDetailView(TestCase):
    def test_invalid_get(self):
        with self.test_client as client:
            response = client.get('/admin/{}'.format(randint(1, 10 ** 9)))
            self.assertEqual(response.status_code, 404, 'Request to unknown game.')

    def test_valid_get(self):
        with self.test_client as client:
            bot_id = loads(client.get('/').data).get('bot_id')
            response = client.get('/admin/{}'.format(bot_id))

            self.assertTrue('text/html' in response.content_type, 'Correct content type.')
            self.assertEqual(response.status_code, 200)

    def test_invalid_delete(self):
        with self.test_client as client:
            r = client.post('/admin/{}'.format(randint(1, 10 ** 9)))
            self.assertEqual(r.status_code, 404, 'Request to unknown game.')

            bot_id = loads(client.get('/').data).get('bot_id')
            r = client.post('/admin/{}'.format(bot_id))
            self.assertEqual(r.status_code, 403, 'Too close to last activity to delete it.')
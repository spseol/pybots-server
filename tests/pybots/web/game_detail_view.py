from datetime import datetime, timedelta
from random import randint

from flask.helpers import url_for
from flask.json import loads
from flask.wrappers import Response

from pybots.game.game import Game
from pybots.game.game_controller import game_controller

from tests.test_case import TestCase


class TestGameDetailView(TestCase):
    def test_invalid_get(self):
        with self.test_client as client:
            response = client.get(url_for('admin_game_detail', bot_id=randint(1, 10 ** 9)))
            self.assertEqual(response.status_code, 404, 'Request to unknown game.')

    def test_valid_get(self):
        with self.test_client as client:
            bot_id = loads(client.get(url_for('init_game')).data).get('bot_id')
            response = client.get(url_for('admin_game_detail', bot_id=bot_id))

            self.assertTrue('text/html' in response.content_type, 'Correct content type.')
            self.assertEqual(response.status_code, 200)

    def test_invalid_delete(self):
        with self.test_client as client:
            r = client.post(url_for('admin_game_delete', bot_id=randint(1, 10 ** 9)))
            self.assertEqual(r.status_code, 404, 'Request to unknown game.')

            bot_id = loads(client.get(url_for('init_game')).data).get('bot_id')
            r = client.post(url_for('admin_game_delete', bot_id=bot_id))
            self.assertEqual(r.status_code, 403, 'Too close to last activity to delete it.')

    def test_valid_single_delete(self):
        with self.test_client as client:
            client.post(url_for('reset'))
            self.assertEqual(len(game_controller.games), 0)
            bot_id = loads(client.get(url_for('init_game')).data).get('bot_id')
            self.assertEqual(len(game_controller.games), 1)

            # START OF HACK
            game = game_controller.games.get(bot_id)
            assert isinstance(game, Game)
            game._last_modified_at = datetime.now() - timedelta(days=1)
            # END OF HACK

            response = client.post(url_for('admin_game_delete', bot_id=bot_id))
            assert isinstance(response, Response)
            self.assertTrue(response.status_code, 302)
            self.assertEqual(len(game_controller.games), 0)

    def test_valid_collective_delete(self):
        with self.test_client as client:
            client.post(url_for('reset'))
            self.assertEqual(len(game_controller.games), 0)
            for _ in range(randint(1, 20)):
                loads(client.get(url_for('init_game')).data).get('bot_id')

            self.assertNotEqual(len(game_controller.games), 0)

            # START OF HACK
            for game in game_controller.games.values():
                game._last_modified_at = datetime.now() - timedelta(minutes=randint(10, 60))
            # END OF HACK

            response = client.post(url_for('admin_game_delete', bot_id=0))
            assert isinstance(response, Response)
            self.assertTrue(response.status_code, 302)
            self.assertEqual(len(game_controller.games), 0)
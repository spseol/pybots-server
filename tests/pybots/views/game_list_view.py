from flask.helpers import url_for
from flask.json import loads

from tests.test_case import TestCase


class TestGameListView(TestCase):
    def test_empty_game_list(self):
        with self.test_client as client:
            client.post(url_for('reset'))

            empty_game_list = loads(client.get(url_for('game_list')).data)
            self.assertIn('games', empty_game_list)
            self.assertIsInstance(empty_game_list.get('games'), list)
            self.assertEqual(len(empty_game_list.get('games')), 0)

    def test_nonempty_game_list(self):
        with self.test_client as client:
            client.post(url_for('reset'))
            bot_id = loads(client.get(url_for('init_game')).data).get('bot_id')

            game_list = loads(client.get(url_for('game_list')).data)
            self.assertIn('games', game_list)
            self.assertIsInstance(game_list.get('games'), list)
            self.assertEqual(len(game_list.get('games')), 1)
            self.assertEqual(game_list.get('games')[0].get('bot_id'), bot_id)

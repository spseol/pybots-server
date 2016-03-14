from random import randint

from flask.json import loads
from flask.wrappers import Response

from pybots.configurations.custom_configuration import CustomConfiguration
from pybots.configurations.default_configuration import DefaultConfiguration
from pybots.game.actions import Action
from pybots.views.response_state import ResponseState
from tests.test_case import TestCase


class TestActionView(TestCase):
    def test_valid_request(self):
        with self.test_client as c:
            bot_id = loads(c.get('/').data).get('bot_id')

            r = c.post('/action', data=dict(bot_id=bot_id, action=Action.TURN_LEFT.value))
            assert isinstance(r, Response)
            self.assertEqual(r.status_code, 200, 'Valid request to turn left.')
            self.assertEqual(r.content_type, 'application/json')
            data = loads(r.data)
            self.assertIn('game', data)

            returned_map = data.get('game')
            self.assertIn('map', returned_map)
            self.assertIn('map_resolutions', returned_map)

    def test_invalid_request(self):
        with self.test_client as c:
            bot_id = loads(c.get('/').data).get('bot_id')

            r = c.post('/action', data=dict(bot_id='', action=''))
            self.assertEqual(r.status_code, 404, 'Request with empty action and bot_id.')

            r = c.post('/action', data=dict(bot_id='foobar', action=Action.TURN_LEFT.value))
            self.assertEqual(r.status_code, 404, 'Request with invalid bot_id.')

            r = c.post('/action', data=dict(bot_id=bot_id, action='foobar'))
            self.assertEqual(r.status_code, 404, 'Request with invalid action.')

    def test_find_wall(self):
        with self.test_client as c:
            bot_id = loads(c.get('/').data).get('bot_id')
            found_wall = False
            for turn in range(DefaultConfiguration.map_height):
                r = c.post('/action', data=dict(bot_id=bot_id, action=Action.STEP.value))
                self.assertEqual(r.status_code, 200)
                if loads(r.data).get('state') in (ResponseState.MOVEMENT_ERROR.state, ResponseState.GAME_WON.state):
                    found_wall = True
                    break

            if not found_wall:
                raise self.failureException('Wall not found or game not finished.')

    def test_two_bots_in_map(self):
        with self.test_client as c:
            c.get('/')  # TODO: remove this get, it's hide dependency on odd request to app
            bot_id_1 = loads(c.get('/').data).get('bot_id')
            bot_id_2 = loads(c.get('/').data).get('bot_id')
            self.assertNotEqual(bot_id_1, bot_id_2, 'Another bots')
            # self.assertListEqual(
            # loads(c.get('/game/{}'.format(bot_id_1)).data).get('map'),
            # loads(c.get('/game/{}'.format(bot_id_2)).data).get('map')
            # )

    def test_unknown_bot(self):
        with self.test_client as c:
            r = c.post('/action', data=dict(bot_id=123456789, action=Action.STEP.value))
            self.assertEqual(r.status_code, 404, 'Request with unknown bot_id.')

    def test_index_post(self):
        map_width, map_height = randint(5, 15), randint(10, 15)
        bots, treasures, blocks = 1, 1, 25
        conf = CustomConfiguration(
            map_width=map_width,
            map_height=map_height,
            bots=bots,
            treasures=treasures,
            blocks=blocks
        )
        with self.test_client as c:
            c.post('/reset')
            c = self.set_conf_to_test_client(conf, c)
            bot_id = loads(c.get('/').data).get('bot_id')
            r = c.get('/game/{}'.format(bot_id))
            data = loads(r.data)

            self.assertEqual(
                map_height,
                len(data.get('map'))
            )
            self.assertEqual(
                map_width,
                len(data.get('map')[0])
            )

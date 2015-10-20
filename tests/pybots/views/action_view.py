from flask.json import loads
from flask.wrappers import Response

from main import app
from pybots.game.actions import Action
from pybots.game.map import Map
from pybots.views.response_state import ResponseState
from tests.pybots_test_case import TestCase


class TestActionView(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_valid_request(self):
        with self.client as c:
            bot_id = loads(c.get('/').data).get('bot_id')

            r = c.post('/action', data=dict(bot_id=bot_id, action=Action.TURN_LEFT.value))
            assert isinstance(r, Response)
            self.assertEqual(r.status_code, 200, 'Valid request to turn left.')
            self.assertEqual(r.content_type, 'application/json')
            data = loads(r.data)
            self.assertIn('map', data)

            returned_map = data.get('map')
            self.assertIn('map', returned_map)
            self.assertIn('map_width', returned_map)
            self.assertIn('map_height', returned_map)
            self.assertIn('map_resolutions', returned_map)

    def test_invalid_request(self):
        with self.client as c:
            bot_id = loads(c.get('/').data).get('bot_id')

            r = c.post('/action', data=dict(bot_id='', action=''))
            self.assertEqual(r.status_code, 404, 'Request with empty action and bot_id.')

            r = c.post('/action', data=dict(bot_id='foobar', action=Action.TURN_LEFT.value))
            self.assertEqual(r.status_code, 404, 'Request with invalid bot_id.')

            r = c.post('/action', data=dict(bot_id=bot_id, action='foobar'))
            self.assertEqual(r.status_code, 404, 'Request with invalid action.')

    def test_find_wall(self):
        with self.client as c:
            bot_id = loads(c.get('/').data).get('bot_id')
            found_wall = False
            for turn in range(Map.DEFAULT_MAP_HEIGHT):
                r = c.post('/action', data=dict(bot_id=bot_id, action=Action.STEP.value))
                self.assertEqual(r.status_code, 200)
                if loads(r.data).get('state') in (ResponseState.MOVEMENT_ERROR.state, ResponseState.GAME_WON.state):
                    found_wall = True
                    break

            if not found_wall:
                raise self.failureException('Wall not found or game not finished.')
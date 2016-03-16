from flask.helpers import url_for

from flask.wrappers import Response

from tests.test_case import TestCase


class TestGameDetailView(TestCase):
    def test_homepage(self):
        with self.test_client as client:
            response = client.get(url_for('index'))
            assert isinstance(response, Response)
            self.assertEqual(response.status_code, 200)
            self.assertIn('text/html', response.content_type)
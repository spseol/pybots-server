from unittest import case

from main import app

from pybots.game.map import Map


class TestCase(case.TestCase):
    @property
    def test_client(self):
        app.testing = True
        return app.test_client()

    def assertIsInMap(self, game_map, field_cls, expected_count=1):
        assert isinstance(game_map, Map)
        count = 0
        inner_map = getattr(game_map, '_{}__map'.format(game_map.__class__.__name__))
        for row in inner_map:
            for field in row:
                if isinstance(field, field_cls):
                    count += 1

        if expected_count != count:
            raise self.failureException('Count of fields is not OK. Expected {}, found {} instances of {}.'.format(
                expected_count, count, field_cls.__name__
            ))
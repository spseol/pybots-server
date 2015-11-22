from unittest.mock import patch

from pybots.configurations.random_configuration import RandomConfiguration

from tests.test_case import TestCase


class TestRandomConfiguration(TestCase):
    def test_random_conf(self):
        conf = RandomConfiguration()
        with patch('random.randint', side_effect=(0, 0, 0)):
            self.assertEqual(conf.map_width, 0)
            self.assertEqual(conf.map_height, 0)
            self.assertEqual(conf.blocks, 0)

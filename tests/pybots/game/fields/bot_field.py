from unittest.case import TestCase

from pybots.game.fields.fields import Fields
from pybots.game.fields.bot_field import BotField
from pybots.game.orientations import Orientation


class TestBotField(TestCase):
    def test_init(self):
        bot = BotField(Orientation.NORTH)
        self.assertEqual(bot.orientation, Orientation.NORTH, 'Bot has to save orientation.')

    def test_export(self):
        bot = BotField(Orientation.NORTH)
        self.assertEqual(bot.export(), Fields.BOT, 'Bot field export')
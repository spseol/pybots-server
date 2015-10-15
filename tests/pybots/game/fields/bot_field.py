from unittest.case import TestCase

from pybots.game.field import Field
from pybots.game.fields.bot_field import BotField
from pybots.game.orientations import Orientation


class TestBotField(TestCase):
    def test_init(self):
        bot = BotField(Orientation.NORTH)
        self.assertEqual(bot.orientation, Orientation.NORTH, 'Bot has to save orientation.')

    def test_export(self):
        bot = BotField(Orientation.NORTH)
        self.assertEqual(bot.export(), Field.BOT, 'Bot field export')
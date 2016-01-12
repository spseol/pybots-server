from random import randint
from unittest.case import TestCase

from pybots.game.field import Field, FIELD_KEY
from pybots.game.fields.battery_bot_field import BatteryBotField, CriticalBatteryLevel


class TestBatteryBotField(TestCase):
    def test_init(self):
        battery_level = randint(0, 100)
        bot = BatteryBotField(battery_level=battery_level)
        self.assertEqual(bot.actual_battery_level, battery_level, 'Bot has to save battery level.')

    def test_export(self):
        battery_level = randint(0, 100)
        bot = BatteryBotField(battery_level=battery_level)
        self.assertEqual(bot.export(), {
            FIELD_KEY: Field.BATTERY_BOT,
            'orientation': BatteryBotField.DEFAULT_ORIENTATION,
            'battery_level': battery_level
        }, 'Battery bot field export.')

    def test_battery_setter(self):
        battery_level = randint(0, 100)
        bot = BatteryBotField(battery_level=battery_level)

        with self.assertRaises(CriticalBatteryLevel):
            while True:
                bot.drain()

    def test_battery_draining(self):
        battery_level = randint(10, 100)
        bot = BatteryBotField(battery_level=battery_level)
        bot.drain()
        self.assertEqual(bot.actual_battery_level, battery_level - 1)

        bot.drain(2)
        self.assertEqual(bot.actual_battery_level, battery_level - 1 - 2)

    def test_battery_charging(self):
        battery_level = randint(10, 100)
        bot = BatteryBotField(battery_level=battery_level)
        bot.charge()
        self.assertEqual(bot.actual_battery_level, battery_level + 1)

        bot.charge(2)
        self.assertEqual(bot.actual_battery_level, battery_level + 1 + 2)
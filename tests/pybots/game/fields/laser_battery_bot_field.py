from random import randint
from unittest.case import TestCase

from pybots.game.field import Field, FIELD_KEY
from pybots.game.fields.laser_battery_bot_field import LaserBatteryBotField, CriticalBatteryLevel


class TestLaserBatteryBotField(TestCase):
    def test_init(self):
        battery_level = randint(0, 100)
        bot = LaserBatteryBotField(battery_level=battery_level)
        self.assertEqual(bot.actual_battery_level, battery_level, 'Bot has to save battery level.')

    def test_export(self):
        battery_level = randint(0, 100)
        bot = LaserBatteryBotField(battery_level=battery_level, name='Tester')
        self.assertEqual(bot.export(), {
            FIELD_KEY: Field.BATTERY_BOT,
            'orientation': LaserBatteryBotField.DEFAULT_ORIENTATION,
            'battery_level': battery_level,
            'name': 'Tester'
        }, 'Battery bot field export.')

    def test_battery_setter(self):
        battery_level = randint(0, 100)
        bot = LaserBatteryBotField(battery_level=battery_level)

        with self.assertRaises(CriticalBatteryLevel):
            while True:
                bot.drain(1)

    def test_battery_draining(self):
        battery_level = randint(10, 100)
        bot = LaserBatteryBotField(battery_level=battery_level)
        bot.drain(LaserBatteryBotField.DEFAULT_STEP_BATTERY_COST)
        self.assertEqual(bot.actual_battery_level, battery_level - LaserBatteryBotField.DEFAULT_STEP_BATTERY_COST)

        bot.drain(LaserBatteryBotField.DEFAULT_LASER_BATTERY_COST)
        self.assertEqual(bot.actual_battery_level, battery_level -
                         LaserBatteryBotField.DEFAULT_STEP_BATTERY_COST -
                         LaserBatteryBotField.DEFAULT_LASER_BATTERY_COST)

    def test_battery_charging(self):
        battery_level = randint(10, 100)
        bot = LaserBatteryBotField(battery_level=battery_level)
        bot.charge(bot.battery_charge)
        self.assertEqual(bot.actual_battery_level, battery_level + bot.battery_charge)

        bot.charge(2)
        self.assertEqual(bot.actual_battery_level, battery_level + bot.battery_charge + 2)
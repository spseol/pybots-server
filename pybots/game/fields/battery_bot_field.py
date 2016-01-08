from pybots.game.field import FIELD_KEY, Field as FieldEnum
from pybots.game.fields.bot_field import BotField


class BatteryBotField(BotField):
    DEFAULT_BATTERY_LEVEL = 10

    def __init__(self, orientation=BotField.DEFAULT_ORIENTATION, battery_level=DEFAULT_BATTERY_LEVEL):
        super().__init__(orientation)
        assert isinstance(battery_level, int)
        self._actual_battery_level = battery_level

    @property
    def actual_battery_level(self):
        return self._actual_battery_level

    @actual_battery_level.setter
    def actual_battery_level(self, level):
        assert isinstance(level, int)
        if level < 0:
            raise CriticalBatteryLevel()
        self._actual_battery_level = level

    def charge(self, level=1):
        self.actual_battery_level += level

    def drain(self, level=1):
        self.actual_battery_level -= level

    def export(self, *args, **kwargs):
        export = super().export(*args, **kwargs)
        export.update({
            FIELD_KEY: FieldEnum.BATTERY_BOT,
            'battery_level': self.actual_battery_level,
        })
        return export


class CriticalBatteryLevel(Exception):
    pass

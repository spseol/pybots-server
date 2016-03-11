from pybots.game.field import FIELD_KEY, Field as FieldEnum
from pybots.game.fields.bot_field import BotField
from pybots.game.utils import MovementError


class LaserBatteryBotField(BotField):
    DEFAULT_BATTERY_LEVEL = 10
    DEFAULT_LASER_DAMAGE = 4

    DEFAULT_LASER_BATTERY_COST = 2
    DEFAULT_STEP_BATTERY_COST = 1

    def __init__(self,
                 orientation=BotField.DEFAULT_ORIENTATION,
                 battery_level=DEFAULT_BATTERY_LEVEL,
                 laser_damage=DEFAULT_LASER_DAMAGE,
                 laser_battery_cost=DEFAULT_LASER_BATTERY_COST,
                 step_battery_cost=DEFAULT_STEP_BATTERY_COST):
        super().__init__(orientation)
        assert isinstance(battery_level, int)
        self._actual_battery_level = battery_level
        self._laser_battery_cost = laser_battery_cost
        self._laser_damage = laser_damage
        self._step_battery_cost = step_battery_cost

    @property
    def actual_battery_level(self):
        return self._actual_battery_level

    @actual_battery_level.setter
    def actual_battery_level(self, level):
        assert isinstance(level, int)
        if level < 0:
            raise CriticalBatteryLevel('Low battery level.')
        self._actual_battery_level = level

    @property
    def laser_damage(self):
        return self._laser_damage

    @property
    def laser_battery_cost(self):
        return self._laser_battery_cost

    @property
    def step_battery_cost(self):
        return self._step_battery_cost

    def charge(self, level=1):
        self.actual_battery_level += level

    def drain(self, level):
        self.actual_battery_level -= level

    def export(self, *args, **kwargs):
        export = super().export(*args, **kwargs)
        export.update({
            FIELD_KEY: FieldEnum.BATTERY_BOT,
            'battery_level': self.actual_battery_level,
        })
        return export


class CriticalBatteryLevel(MovementError):
    pass

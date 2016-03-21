from pybots.game.field import FIELD_KEY, Field as FieldEnum
from pybots.game.fields.bot_field import BotField
from pybots.game.utils import MovementError


class LaserBatteryBotField(BotField):
    DEFAULT_BATTERY_LEVEL = 10
    DEFAULT_LASER_DAMAGE = 4
    DEFAULT_BATTERY_CHARGE = 1

    DEFAULT_LASER_BATTERY_COST = 2
    DEFAULT_STEP_BATTERY_COST = 1

    def __init__(self,
                 orientation=BotField.DEFAULT_ORIENTATION,
                 battery_level=DEFAULT_BATTERY_LEVEL,
                 laser_damage=DEFAULT_LASER_DAMAGE,
                 laser_battery_cost=DEFAULT_LASER_BATTERY_COST,
                 step_battery_cost=DEFAULT_STEP_BATTERY_COST,
                 battery_charge=DEFAULT_BATTERY_CHARGE,
                 name=''):
        super().__init__(orientation, name)
        assert isinstance(battery_level, int), 'Actual battery level for bot.'
        assert isinstance(laser_damage, int), 'Damage for bots\'s laser'
        assert isinstance(laser_battery_cost, int), 'Cost of battery of firing laser'
        assert isinstance(step_battery_cost, int), 'Cost of battery for bot step'
        assert isinstance(battery_charge, int), 'Value of unit of bot charge'
        self._actual_battery_level = battery_level
        self._laser_battery_cost = laser_battery_cost
        self._laser_damage = laser_damage
        self._step_battery_cost = step_battery_cost
        self._battery_charge = battery_charge

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

    @property
    def battery_charge(self):
        return self._battery_charge

    def charge(self, level=1):
        self.actual_battery_level += level

    def drain(self, level):
        self.actual_battery_level -= level

    def export(self, *args, **kwargs):
        export = super().export(*args, **kwargs)
        export.update({
            FIELD_KEY: FieldEnum.LASER_BATTERY_BOT,
            'battery_level': self.actual_battery_level,
        })
        return export


class CriticalBatteryLevel(MovementError):
    pass

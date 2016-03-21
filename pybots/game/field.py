from enum import unique, IntEnum

FIELD_KEY = 'field'


@unique
class Field(IntEnum):
    EMPTY = 0
    TREASURE = 1
    BOT = 2
    BLOCK = 3
    LASER_BATTERY_BOT = 4

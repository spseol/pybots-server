from enum import unique, IntEnum


@unique
class Action(IntEnum):
    STEP = 0
    TURN_LEFT = 1
    TURN_RIGHT = 2

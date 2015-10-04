from enum import Enum, unique


@unique
class Action(Enum):
    STEP = 0
    TURN_LEFT = 1
    TURN_RIGHT = 2

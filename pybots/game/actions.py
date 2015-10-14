from enum import unique, Enum


@unique
class Action(Enum):
    STEP = 'step'
    TURN_LEFT = 'turn_left'
    TURN_RIGHT = 'turn_right'

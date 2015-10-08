from enum import unique, IntEnum


@unique
class Orientation(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

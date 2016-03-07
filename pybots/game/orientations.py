from enum import unique, IntEnum


@unique
class Orientation(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @property
    def is_horizontal(self):
        return self in (Orientation.EAST, Orientation.WEST)

    @property
    def is_vertical(self):
        return not self.is_horizontal

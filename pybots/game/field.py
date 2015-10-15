from enum import IntEnum, unique


@unique
class Field(IntEnum):
    EMPTY = 0
    TREASURE = 1
    BOT = 2

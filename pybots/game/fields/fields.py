from enum import IntEnum, unique


@unique
class Fields(IntEnum):
    # TODO: rename to Field
    EMPTY = 0
    TREASURE = 1
    BOT = 2

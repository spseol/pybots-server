from abc import ABCMeta, abstractmethod
import random

from pybots.game.actions import Action
from pybots.game.orientations import Orientation


class Exportable(metaclass=ABCMeta):
    @abstractmethod
    def export(self, *args, **kwargs):
        pass


def get_next_position(position, orientation):
    assert isinstance(orientation, Orientation)
    assert isinstance(position, (list, tuple)) and len(position) == 2

    x, y = position
    if orientation == Orientation.NORTH:
        return x, y - 1
    elif orientation == Orientation.EAST:
        return x + 1, y
    elif orientation == Orientation.SOUTH:
        return x, y + 1
    elif orientation == Orientation.WEST:
        return x - 1, y


def get_next_orientation(orientation, action):
    assert isinstance(orientation, Orientation)
    assert isinstance(action, Action)

    if action == Action.TURN_RIGHT:
        return Orientation(divmod(orientation.value + 1, 4)[1])
    elif action == Action.TURN_LEFT:
        return Orientation(divmod(orientation.value - 1, 4)[1])


def get_positions_in_row(game_map, position, orientation, limit=None):
    from pybots.game.map import OutOfMapError, Map

    assert isinstance(orientation, Orientation)
    assert isinstance(position, (list, tuple)) and len(position) == 2
    assert isinstance(game_map, Map)
    assert limit is None or (isinstance(limit, int) and limit >= 0)

    i = 0
    while True:
        position = get_next_position(position, orientation)
        try:
            game_map.__getitem__(position)
            yield position
            i += 1
            if limit is not None and i == limit:
                return
        except OutOfMapError:
            break


def random_position(game_map):
    return random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1)

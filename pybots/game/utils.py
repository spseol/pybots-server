from abc import ABCMeta, abstractmethod

from pybots.game.actions import Action
from pybots.game.orientations import Orientation


class Exportable(metaclass=ABCMeta):
    @abstractmethod
    def export(self):
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

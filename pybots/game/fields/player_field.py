from pybots.game.actions import Action
from pybots.game.fields.field import Field
from pybots.game.fields.fields import Fields
from pybots.game.orientations import Orientation
from pybots.game.utils import get_next_orientation


class PlayerField(Field):
    def __init__(self, orientation):
        assert isinstance(orientation, Orientation)
        self._orientation = orientation

    def export(self):
        # TODO: fix JSON serializing enum
        return Fields.PLAYER.value

    @property
    def orientation(self):
        return self._orientation

    def rotate(self, action):
        assert isinstance(action, Action)
        self._orientation = get_next_orientation(
            self._orientation,
            action
        )

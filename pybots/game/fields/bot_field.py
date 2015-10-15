from pybots.game.actions import Action
from pybots.game.fields.field import Field
from pybots.game.field import Field as FieldEnum
from pybots.game.orientations import Orientation
from pybots.game.utils import get_next_orientation


class BotField(Field):
    DEFAULT_ORIENTATION = Orientation.NORTH

    def __init__(self, orientation=DEFAULT_ORIENTATION):
        assert isinstance(orientation, Orientation)
        self._orientation = orientation

    def export(self):
        return FieldEnum.BOT

    @property
    def orientation(self):
        return self._orientation

    def rotate(self, action):
        assert isinstance(action, Action)
        self._orientation = get_next_orientation(
            self._orientation,
            action
        )

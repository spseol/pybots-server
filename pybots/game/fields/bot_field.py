from pybots.game.actions import Action
from pybots.game.fields.field import Field
from pybots.game.field import Field as FieldEnum, FIELD_KEY
from pybots.game.orientations import Orientation
from pybots.game.utils import get_next_orientation


class BotField(Field):
    DEFAULT_ORIENTATION = Orientation.NORTH

    def __init__(self,
                 orientation=DEFAULT_ORIENTATION,
                 name=''):
        assert isinstance(orientation, Orientation), 'orientation is instance of Orientation'
        assert isinstance(name, str), 'bot name of str type'
        self._orientation = orientation
        self._name = name

    def export(self, *args, **kwargs):
        return {
            FIELD_KEY: FieldEnum.BOT,
            'orientation': self.orientation,
            'name': self._name
        }

    @property
    def orientation(self):
        return self._orientation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def rotate(self, action):
        assert isinstance(action, Action)
        self._orientation = get_next_orientation(
            self._orientation,
            action
        )

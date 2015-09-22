from inspect import isclass

from pybots.game.fields.empty_field import EmptyField
from pybots.game.fields.field import Field


class Map(object):
    DEFAULT_MAP_WIDTH = 4
    DEFAULT_MAP_HEIGHT = 4

    def __init__(self,
                 width=DEFAULT_MAP_WIDTH,
                 height=DEFAULT_MAP_HEIGHT,
                 default_field=EmptyField):
        super(self.__class__, self).__init__()
        assert isinstance(width, int) and width >= 1, 'Invalid map width'
        assert isinstance(height, int) and height >= 1, 'Invalid map height'
        assert isclass(default_field) and issubclass(default_field, Field), 'Unknown default field'

        self.__map = [[default_field() for _x in range(width)] for _y in range(height)]
        self.__width = width
        self.__height = height

    def __getitem__(self, index):
        return self._getitem(index)

    def __setitem__(self, index, field):
        self._getitem(index)
        if not isinstance(field, Field):
            raise UnknownFieldError('Cannot set this field.', field)
        self.__map[index[1]][index[0]] = field

    def export_map(self):
        return [[self._export_field(field) for field in row] for row in self.__map]

    def _getitem(self, index):
        assert isinstance(index, (list, tuple)) and len(index) == 2, 'Index has to have two items, x and y.'
        try:
            return self.__map[index[1]][index[0]]
        except IndexError as e:
            raise OutOfMapError(e)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @classmethod
    def _export_field(cls, field):
        if isinstance(field, Field):
            return field.export()
        raise UnknownFieldError('Cannot export this unknown field.', field)


class OutOfMapError(IndexError):
    pass


class UnknownFieldError(TypeError):
    pass

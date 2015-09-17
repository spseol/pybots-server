from pybots.game.empty_field import EmptyField
from pybots.game.field import Field


class Map(object):
    DEFAULT_MAP_WIDTH = 10
    DEFAULT_MAP_HEIGHT = 10

    def __init__(self, width=DEFAULT_MAP_WIDTH, height=DEFAULT_MAP_HEIGHT):
        super(self.__class__, self).__init__()
        assert isinstance(width, int) and width >= 1, 'Invalid map width'
        assert isinstance(height, int) and height >= 1, 'Invalid map height'

        self.__map = [[EmptyField() for _x in range(width)] for _y in range(height)]
        self.__width = width
        self.__height = height

    def __getitem__(self, index):
        assert isinstance(index, (list, tuple)) and len(index) == 2, 'Index has to have two items, x and y.'
        try:
            row = self.__map[index[1]]
            return row[index[0]]
        except IndexError as e:
            raise OutOfMapError(e)

    def export_map(self):
        return [[self._export_field(field) for field in row] for row in self.__map]

    def _export_field(self, field):
        if isinstance(field, Field):
            return field.export()
        raise UnknownFieldError()


class OutOfMapError(IndexError):
    pass


class UnknownFieldError(TypeError):
    pass

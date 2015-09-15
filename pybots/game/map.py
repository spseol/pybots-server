class Map(object):
    DEFAULT_MAP_WIDTH = 10
    DEFAULT_MAP_HEIGHT = 10

    def __init__(self, width=DEFAULT_MAP_WIDTH, height=DEFAULT_MAP_HEIGHT):
        super(self.__class__, self).__init__()
        self.__map = [[None for _x in range(width)] for _y in range(height)]
        self.__width = width
        self.__height = height

    def __getitem__(self, index):
        assert isinstance(index, (list, tuple)) and len(index) == 2, 'Index has to have two items, x and y.'
        try:
            row = self.__map[index[1]]
            return row[index[0]]
        except IndexError as e:
            raise OutOfMapError(e)


class OutOfMapError(IndexError):
    pass
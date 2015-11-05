from abc import ABCMeta

from pybots.game.fields.empty_field import EmptyField


class BaseConfiguration(metaclass=ABCMeta):
    map_width = None
    map_height = None
    default_empty_map_field = EmptyField
    bots = None
    treasures = None
    blocks = None

    _fields = (
        ('map_width', int),
        ('map_height', int),
        ('bots', int),
        ('treasures', int),
        ('blocks', int),
        ('default_empty_map_field', type)
    )

    def __init__(self):
        missing = []
        for field in self._fields:
            if not hasattr(self, field[0]):
                missing.append(field[0])
                continue

            if getattr(self, field[0], None) is None:
                missing.append(field[0])
                continue

            if field[1]:
                if not isinstance(getattr(self, field[0], None), field[1]):
                    missing.append(field[0])
                    continue

        if missing:
            raise ConfigurationError("Please provide all configuration fields, '{}' not found or isn't in correct type."
                                     .format(', '.join(missing)), missing)


class ConfigurationError(Exception):
    pass

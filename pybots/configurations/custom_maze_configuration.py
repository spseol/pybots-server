from pybots.configurations.base_configuration import BaseConfiguration
from pybots.configurations.custom_configuration import CustomConfiguration
from pybots.configurations.maze_field_placer import MazeFieldPlacerMixin


class CustomMazeConfiguration(BaseConfiguration, MazeFieldPlacerMixin):
    default_empty_map_field = CustomConfiguration.default_empty_map_field

    __init__ = CustomConfiguration.__init__

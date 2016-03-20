from pybots.configurations import ConfigurationError
from pybots.configurations.custom_configuration import CustomConfiguration
from pybots.configurations.custom_maze_configuration import CustomMazeConfiguration
from pybots.game.map_factory import MapFactory
from wtforms import Form
from wtforms.fields.core import BooleanField
from wtforms.fields.html5 import IntegerField
from wtforms.validators import DataRequired, NumberRange


class ConfigurationForm(Form):
    map_width = IntegerField('map width', validators=(DataRequired(), NumberRange(5, 100)), filters=(int, ))
    map_height = IntegerField('map height', validators=(DataRequired(), NumberRange(5, 100)), filters=(int, ))
    blocks = IntegerField('count of blocks', validators=(DataRequired(), NumberRange(5 ** 2, 100 ** 2)),
                          filters=(int, ))
    treasures = IntegerField('count of treasures', validators=(DataRequired(), NumberRange(1, 5)), filters=(int, ))
    bots = IntegerField('count of bots', validators=(DataRequired(), NumberRange(1, 5)), filters=(int, ))
    rounded_game = BooleanField('game by rounds', default=False, validators=(), filters=(bool, ))
    maze_game = BooleanField('maze game', default=False, validators=(), filters=(bool, ))
    battery_game = BooleanField('battery game', default=False, validators=(), filters=(bool, ))
    laser_game = BooleanField('laser game', default=False, validators=(), filters=(bool, ))

    @property
    def as_configuration(self):
        if self.data.get('maze_game'):
            return CustomMazeConfiguration(**self.data)
        return CustomConfiguration(**self.data)

    def validate(self):
        if not super().validate():
            return False

        try:
            MapFactory.create(self.as_configuration)
        except ConfigurationError as e:
            self.bots.errors.append(str(e))
            return False

        return True

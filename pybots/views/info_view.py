from flask.json import jsonify
from flask.views import MethodView

from pybots.game.actions import Action
from pybots.game.orientations import Orientation
from pybots.game.field import Field
from pybots.views.response_state import ResponseState


class InfoView(MethodView):
    def get(self, *args, **kwargs):
        def enum_info_dict(enum):
            return {
                str(member.name): list(member.value) if isinstance(member.value, tuple) else str(member.value)
                for member in enum
            }

        return jsonify(**{
            Action.__name__.lower(): enum_info_dict(Action),
            Orientation.__name__.lower(): enum_info_dict(Orientation),
            Field.__name__.lower(): enum_info_dict(Field),
            ResponseState.__name__.lower(): enum_info_dict(ResponseState)
        }), 200

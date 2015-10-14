from flask.json import jsonify
from flask.views import MethodView

from pybots.game.actions import Action
from pybots.game.orientations import Orientation
from pybots.game.fields.fields import Fields


class InfoView(MethodView):
    def get(self, *args, **kwargs):
        def enum_info_dict(enum):
            return {str(member.name): str(member.value) for member in enum}

        return jsonify(
            action=enum_info_dict(Action),
            orientation=enum_info_dict(Orientation),
            fields=enum_info_dict(Fields)
        ), 200

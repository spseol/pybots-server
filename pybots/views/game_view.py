from flask.json import jsonify

from flask.views import View

from pybots.game.game_controller import GameController

from pybots.game.map import Map


class GameView(View):
    def dispatch_request(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        if not user_id:
            return 'Invalid request', 404

        # TODO: delegate to GameController
        game_map = GameController.maps.get(user_id, None)

        if user_id not in GameController.maps:
            return 'Unknown user_id', 404

        assert isinstance(game_map, Map)
        return jsonify(map=game_map.export_map())

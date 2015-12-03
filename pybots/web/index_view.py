from datetime import datetime

from flask.helpers import url_for
from flask.templating import render_template
from flask.views import MethodView
from werkzeug.utils import redirect

from pybots.configurations.configuration_provider import configuration_provider
from pybots.game.game_controller import game_controller
from pybots.views.utils import form_to_kwargs
from pybots.web.forms import ConfigurationForm
from pybots.web.game_detail_view import GameDetailView


class IndexView(MethodView):
    decorators = [form_to_kwargs]

    def get(self):
        conf_form = ConfigurationForm(obj=configuration_provider.actual)
        return render_template('index.html',
                               games=game_controller.sorted_games(),
                               now=datetime.now(),
                               form=conf_form,
                               set=set,
                               TIMEOUT_DELETE=GameDetailView.TIMEOUT_DELETE)

    def post(self, **kwargs):
        form = ConfigurationForm(data=kwargs)
        if form.validate():
            configuration_provider.actual = form.as_configuration
            return redirect(url_for('admin_index'))

        return render_template('index.html',
                               games=game_controller.sorted_games(),
                               now=datetime.now(),
                               form=form,
                               set=set,
                               TIMEOUT_DELETE=GameDetailView.TIMEOUT_DELETE)

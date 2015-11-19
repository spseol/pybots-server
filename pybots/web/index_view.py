from flask.helpers import url_for

from flask.templating import render_template

from flask.views import MethodView

from werkzeug.utils import redirect

from pybots.configurations.configuration_provider import configuration_provider

from pybots.game.game_controller import game_controller

from pybots.views.utils import form_to_kwargs

from pybots.web.forms import ConfigurationForm


class IndexView(MethodView):
    decorators = [form_to_kwargs]

    def get(self):
        conf_form = ConfigurationForm(obj=configuration_provider.actual)
        return render_template('index.html',
                               games=game_controller.games,
                               form=conf_form)

    def post(self, **kwargs):
        form = ConfigurationForm(data=kwargs)
        if form.validate():
            configuration_provider.actual = form.as_configuration
            return redirect(url_for('admin_index'))

        return render_template('index.html',
                               games=game_controller.games,
                               form=form)

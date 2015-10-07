from werkzeug.urls import url_encode

from main import app

from pybots.views.utils import args_to_kwargs, form_to_kwargs
from tests.pybots.pybots_test_case import TestCase


class UtilsView(TestCase):
    def test_args_to_kwargs(self):
        params = dict(foo='bar', bar='foo', c='6')

        def view(**kwargs):
            self.assertDictEqual(params, kwargs)

        with app.test_request_context('/?{}'.format(url_encode(params))):
            decorated = args_to_kwargs(view)
            decorated()

    def test_form_to_kwargs(self):
        params = dict(bar='bar', foo='foo', ba='5')

        def view(**kwargs):
            self.assertDictEqual(params, kwargs)

        with app.test_request_context('/', method='POST', data=params):
            decorated = form_to_kwargs(view)
            decorated()

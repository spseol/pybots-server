from os.path import join, dirname

from flask_misaka import markdown

from flask.templating import render_template
from flask.views import MethodView

import pybots


class IndexView(MethodView):
    def get(self):
        with open(join(dirname(pybots.__file__), '../README.md')) as f:
            readme_md = '\n\r'.join(f.readlines()).replace('```json', '').replace('```', '').replace('{',
                                                                                                     "\t{").replace('}',
                                                                                                                    "\t}")
            readme_html = markdown(
                readme_md,
                autolink=True,
                disable_indented_code=False,
            )
            return render_template('index.html', readme_html=readme_html)

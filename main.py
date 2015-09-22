from flask import Flask

from pybots.urls import urls


app = Flask(__name__)

if __name__ == '__main__':
    for rule, view in urls:
        app.add_url_rule(rule, view_func=view)
    app.run(debug=True)
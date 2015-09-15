from time import sleep

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    yield 'request {} started'
    sleep(5)
    yield 'request {} end'
    return ''


if __name__ == '__main__':
    app.run(debug=True, processes=2)

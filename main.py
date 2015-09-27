#!/usr/bin/env python

import sys
from flask import Flask
from pybots.urls import urls

PORT=44822


app = Flask(__name__)

if __name__ == '__main__':
    for rule, view in urls:
        app.add_url_rule(rule, view_func=view)
    if len(sys.argv) > 1 and sys.argv[1].upper() == 'DEBUG':
        app.run(host='127.0.0.1', port=PORT,  debug=True)
    else:
        app.run(host='0.0.0.0', port=PORT,  debug=False)

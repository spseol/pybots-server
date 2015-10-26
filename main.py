#!/usr/bin/env python3
from logging import getLogger
from logging.handlers import RotatingFileHandler
import sys
import os
from os.path import join

from pybots.json_encoder import JSONEncoder


if sys.version_info < (3, ):
    print('Pybots require python 3.')
    exit(1)

import logging
import logging.handlers

from flask import Flask

from pybots.urls import urls


PORT = 44822

app = Flask(__name__)

app.json_encoder = JSONEncoder
for rule, view in urls:
    app.add_url_rule(rule, view_func=view)


def run():
    if len(sys.argv) > 1 and sys.argv[1].upper() == 'DEBUG':
        app.run(host='127.0.0.1', port=PORT, debug=True)
    else:
        logger = getLogger()  # app.logger
        # TODO: use default Flask logger
        logger.setLevel(logging.DEBUG)

        log_dir = os.path.dirname(__file__)
        file_handler = RotatingFileHandler(join(log_dir, 'robots.log'),
                                           maxBytes=5000,
                                           backupCount=7)

        console_handler = logging.StreamHandler()

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        app.run(host='0.0.0.0', port=PORT, debug=False, threaded=True)


if __name__ == '__main__':
    run()

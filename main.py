#!/usr/bin/env python3
import sys
from flask import Flask
from pybots.urls import urls
import logging
import logging.handlers

PORT = 44822

app = Flask(__name__)

if __name__ == '__main__':
    for rule, view in urls:
        app.add_url_rule(rule, view_func=view)
    if len(sys.argv) > 1 and sys.argv[1].upper() == 'DEBUG':
        app.run(host='127.0.0.1', port=PORT,  debug=True)
    else:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # fileHandler = logging.FileHandler("robots.log")
        fileHandler = logging.handlers.RotatingFileHandler("robots.log",
                                                           maxBytes=5000,
                                                           backupCount=7)

        consoleHandler = logging.StreamHandler()
        '''
        logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] "
                                         "[%(levelname)-5.5s]  %(message)s")
        fileHandler.setFormatter(logFormatter)
        consoleHandler.setFormatter(logFormatter)
        '''
        logger.addHandler(fileHandler)
        logger.addHandler(consoleHandler)

        app.run(host='0.0.0.0', port=PORT,  debug=False)

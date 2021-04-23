import logging
import sys
from http import HTTPStatus
from logging.config import dictConfig

import json_log_formatter
from flask import Flask, request
from pythonjsonlogger import jsonlogger

formatter = json_log_formatter.JSONFormatter()
json_handler = logging.StreamHandler()
json_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)s %(levelname)s:%(message)s')
#
# logger = logging.getLogger(__name__)
# logHandler = logging.StreamHandler()
# formatter = jsonlogger.JsonFormatter()
# logHandler.setFormatter(formatter)
# logger.addHandler(logHandler)

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    args = request.get_json()

    user = args['username']
    logger.info(f'{user} logged in successfully',
                extra={
                    'job_category': 'test_function',
                    'logger.name': 'my_json'
        })
    return {}, HTTPStatus.OK


if __name__ == '__main__':
    app.run(debug=False)

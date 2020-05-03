from http import HTTPStatus

from flask_app.src.processors.history import get_history
from flask_app.src import json


@json()
def get_handler():
    return get_history(), HTTPStatus.ACCEPTED

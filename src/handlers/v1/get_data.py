from http import HTTPStatus

from src.processors.history import get_history
from src.utils import json


@json()
def get_handler():
    return get_history(), HTTPStatus.ACCEPTED

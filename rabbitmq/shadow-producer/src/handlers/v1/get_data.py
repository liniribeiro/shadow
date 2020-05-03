from http import HTTPStatus

from celery import current_app
from flask import request

from src.utils import json


@json()
def get_handler():

    return None, HTTPStatus.ACCEPTED

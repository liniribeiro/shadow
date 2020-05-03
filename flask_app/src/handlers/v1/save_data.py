from http import HTTPStatus

from flask_app.src.database.queries import save
from flask_app.src.schemas import SaveInput
from flask_app.src import validate, json


@json()
@validate(request_class=SaveInput)
def save_handler(body, **kwargs):
    save(body['data']['album'])
    return None, HTTPStatus.ACCEPTED

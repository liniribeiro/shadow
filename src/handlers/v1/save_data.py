from http import HTTPStatus

from src.database.queries import save
from src.schemas.save import SaveInput
from src.utils import validate, json


@json()
@validate(request_class=SaveInput)
def save_handler(body, **kwargs):
    save(body['data']['album'])
    return None, HTTPStatus.ACCEPTED

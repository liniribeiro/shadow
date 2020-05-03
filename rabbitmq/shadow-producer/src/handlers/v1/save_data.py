from http import HTTPStatus

from celery import current_app
from src.schemas.save import SaveDocumentsInput
from src.utils import validate, json


@json()
@validate(request_class=SaveDocumentsInput)
def save_handler(body, **kwargs):
    return None, HTTPStatus.ACCEPTED

from functools import wraps
from typing import Type

import ujson as ujson
from flask import request, Response
from pydantic import BaseModel


def validate(
    request_class: Type[BaseModel] = None, response_class: Type[BaseModel] = None
):
    def internal_validate(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            body = request.json
            if request_class:
                request_class.validate(body)
            kwargs.setdefault("body", body)
            kwargs.update(request.args.to_dict())
            result, status = fn(*args, **kwargs)
            if response_class:
                response_class.validate(result)
            return result, status

        return wrapper

    return internal_validate


def json():
    def internal_json(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result, status = fn(*args, **kwargs)
            return Response(
                response=ujson.dumps(result) if result else None,
                status=status,
                content_type="application/json",
            )

        return wrapper

    return internal_json

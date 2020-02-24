from flask import Blueprint

from src.handlers.v1.get_data import get_handler

from src.handlers.v1.save_data import save_handler


api_v1 = Blueprint("api.v1", __name__)
api_v1.add_url_rule(
    "/get",
    endpoint="GetHandler",
    view_func=get_handler,
    methods=["GET"],
)

api_v1.add_url_rule(
    "/save",
    endpoint="SaveHandler",
    view_func=save_handler,
    methods=["POST"],
)

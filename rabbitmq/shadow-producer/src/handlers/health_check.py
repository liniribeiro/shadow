from flask import jsonify


def health_check_handler():
    return jsonify(None), 200

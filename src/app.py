from flask import Flask

from src.database import db, migration
from src.handlers.health_check import health_check_handler
from src.handlers.v1 import api_v1
from src.settings import (
    APP_DEFAULT_HOST,
    APP_DEFAULT_PORT,
    BASE_PATH,
    DEBUG, DatabaseSettings)


def make_app() -> Flask:
    flask = Flask(__name__)
    flask.url_map.strict_slashes = False
    flask.add_url_rule(
        f"{BASE_PATH}/health-check", view_func=health_check_handler, methods=["GET"]
    )
    flask.register_blueprint(api_v1, url_prefix=f"{BASE_PATH}/v1")
    flask.config['SQLALCHEMY_DATABASE_URI'] = DatabaseSettings.DATABASE_URI
    flask.config['SQLALCHEMY_ECHO'] = DEBUG
    flask.config['SQLALCHEMY_BINDS'] = {'slave': DatabaseSettings.REPLICA_DATABASE_URI}

    flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(flask)

    migration.upgrade()

    return flask


app = make_app()


if __name__ == "__main__":
    app.run(host=APP_DEFAULT_HOST, port=APP_DEFAULT_PORT, debug=DEBUG)


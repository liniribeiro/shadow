from typing import Dict

from flask_app.src import replica_session
from flask_app.src.database.queries import get_count


def get_history() -> Dict:
    with replica_session() as session:
        return dict(get_count(session))

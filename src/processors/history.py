from typing import Dict

from src.database import replica_session
from src.database.queries import get_count, get_all


def get_history() -> Dict:
    with replica_session() as session:
        return dict(get_count(session))

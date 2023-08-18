from typing import List, Tuple

import ibm_db
from src.globals import ConfigAndResourcesManager


def connect_to_db2(config_and_resources_manager: ConfigAndResourcesManager):
    db = config_and_resources_manager.get('DatabaseSection', 'db2_db')
    return ibm_db.db2.connect(db)


def _execute_db2_query(conn, query: str, params=None) -> List[Tuple]:
    cursor = conn.cursor()
    if params is None:
        cursor.execute(query)
    else:
        cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result

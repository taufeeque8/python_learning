import os
from typing import List, Tuple

import ibm_db
import pyodbc as pyodbc

from src.globals import ConfigAndResourcesManager


def connect_to_db(database, hostname, port, username, password):
    conn_str = f"DATABASE={database};HOSTNAME={hostname};PORT={port};PROTOCOL=TCPIP;UID={username};PWD={password};"
    conn = ibm_db.connect(conn_str, '', '')
    return conn

def execute_query(conn, query,params)-> List[Tuple]:
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_load_id(db2_conn, solr_file_name: str):
    query = "SELECT LOAD_ID FROM DOCPLATFORM.FILESPLITTING_INFO_TABLE WHERE OUTPUT_FILE_PATH LIKE ?"
    params=(f"%{solr_file_name}")
    return  execute_query(db2_conn, query, params)

def _run_mssql_stored_procedure(mssql_connection: pyodbc.Connection, query: str, params:Tuple) -> None:
    cursor = mssql_connection.cursor()
    try:
        cursor.execute(query, params)
        cursor.commit()
        cursor.close()
    except Exception as e:
        try:
            cursor.close()
        except Exception:
            pass
        raise e


def update_traces_and_status_of_load_ids(mssql_connection: pyodbc.Connection, load_ids: List[str] )-> None:
    query = "exec sp akhthi"
    params =(','.join(load_ids))
    _run_mssql_stored_procedure(mssql_connection,query,params)


def connect_to_mssql(config_and_resources_manager: ConfigAndResourcesManager) -> pyodbc.Connection:

    os.environ["ODBCSYSINI"] = config_and_resources_manager.get('DatabaseSection", ODBCSYSINI_dir')
    os.environ["FREETDSCONF"] = config_and_resources_manager.get('DatabaseSection','FREETDSCONF_file')
    database = config_and_resources_manager.get('DatabaseSection', 'mssql_db')
    driver = config_and_resources_manager.get('DatabaseSection', 'posix_driver')
    server= config_and_resources_manager.get('DatabaseSection', 'mssql_server_name')
    connection_string = f'DRIVER={driver}; SERVERNAME={server}; DATABASE={database};'

    return pyodbc.connect(connection_string)
# import pyodbc
#
import pyodbc

from src.db1 import connect_to_db2
from src.db2 import connect_to_mssql
from src.globals import ConfigAndResourcesManager as config_and_resource_manager

_mssql_conn: pyodbc.Connection = connect_to_mssql(config_and_resource_manager)
_db2_conn = connect_to_db2(config_and_resource_manager)

def clean_up():
    _mssql_conn.close()
    _db2_conn.close()


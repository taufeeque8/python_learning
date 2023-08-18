#

import unittest
from unittest import mock
from src.db_wrapper import clean_up


class CleanUpTestCase(unittest.TestCase):

    @mock.patch('src.db_wrapper.connect_to_mssql')
    @mock.patch('src.db_wrapper.connect_to_db2')
    def test_clean_up(self, mock_connect_to_db2, mock_connect_to_mssql):
        mock_mssql_conn = mock.Mock()
        mock_db2_conn = mock.Mock()

        mock_connect_to_mssql.return_value = mock_mssql_conn
        mock_connect_to_db2.return_value = mock_db2_conn

        clean_up()

        mock_connect_to_mssql.assert_called_once()
        mock_connect_to_db2.assert_called_once()

        mock_mssql_conn.close.assert_called_once()
        mock_db2_conn.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()

#
# import pytest
# from unittest import mock
#
# from src.db_wrapper import clean_up
#
# @pytest.fixture
# def mock_connections():
#     mssql_conn_mock = mock.Mock()
#     db2_conn_mock = mock.Mock()
#
#     def connect_to_mssql_mock(config_and_resource_manager):
#         return mssql_conn_mock
#
#     def connect_to_db2_mock(config_and_resource_manager):
#         return db2_conn_mock
#
#     with mock.patch('src.db_wrapper.connect_to_db2', new=connect_to_db2_mock):
#         with mock.patch('src.db_wrapper.pyodbc.connect', return_value=mssql_conn_mock):
#             yield mssql_conn_mock, db2_conn_mock
#
# def test_clean_up(mock_connections):
#     mssql_conn_mock, db2_conn_mock = mock_connections
#
#     clean_up()
#
#     mssql_conn_mock.close.assert_called_once()
#     db2_conn_mock.close.assert_called_once()

import unittest
from unittest.mock import patch, MagicMock


class TestDatabaseConnections(unittest.TestCase):

    @patch('src.db2.connect_to_mssql')
    @patch('src.db1.connect_to_db2')
    def test_clean_up(self, mock_db2_conn, mock_mssql_conn):
        mssql_conn = MagicMock()
        db2_conn = MagicMock()
        mock_db2_conn.return_value = db2_conn
        mock_mssql_conn.return_value = mssql_conn
        from src.db_wrapper import clean_up
        clean_up()
        mock_db2_conn.assert_called_once()
        mock_mssql_conn.assert_called_once()

        # # Assertions
        # self.assertEqual(_mssql_conn, 'Mock MSSQL Connection')
        # self.assertEqual(_db2_conn, 'Mock DB2 Connection')
#
#     def test_clean_up(self):
#         # Mock connections
#         mssql_conn_mock = unittest.mock.Mock()
#         db2_conn_mock = unittest.mock.Mock()
#
#         # Assign mocks to the connections
#         with patch('__main__._mssql_conn', mssql_conn_mock), \
#              patch('__main__._db2_conn', db2_conn_mock):
#
#             # Call the function to be tested
#             clean_up()
#
#             # Assertions
#             mssql_conn_mock.close.assert_called_once()
#             db2_conn_mock.close.assert_called_once()
# #
# # if __name__ == '__main__':
# #     unittest.main()
# #
# # # import pytest
# # # from unittest.mock import Mock, patch
# # # from src.db_wrapper import clean_up
# # #
# # # @pytest.fixture(autouse=True)
# # # def mock_connections():
# # #     with patch('src.db2.connect_to_mssql') as mock_mssql, \
# # #          patch('src.db1.connect_to_db2') as mock_db2:
# # #         yield mock_mssql.return_value, mock_db2.return_value
# # #
# # # def test_clean_up(mock_connections):
# # #     mssql_conn, db2_conn = mock_connections
# # #
# # #     # Mock the close methods of the connections
# # #     mssql_conn.close = Mock()
# # #     db2_conn.close = Mock()
# # #
# # #     # Call the clean_up function
# # #     clean_up()
# # #
# # #     # Assert that the close methods were called
# # #     assert mssql_conn.close.called
# # #     assert db2_conn.close.called
# #
# #
# #
#
# import pytest
# from unittest import mock
#
# # Import the module containing the code you want to test
# from src.db_wrapper import clean_up
#
# # Define a mock connection object for pyodbc.Connection
# class MockConnection:
#     def close(self):
#         pass
#
# # Define a mock connect_to_mssql function
# def mock_connect_to_mssql(config_and_resource_manager):
#     return MockConnection()
#
# # Define a mock connect_to_db2 function
# def mock_connect_to_db2(config_and_resource_manager):
#     return MockConnection()
#
# # Test the clean_up function
# def test_clean_up(monkeypatch):
#     # Patch the connect_to_mssql and connect_to_db2 functions with the mocks
#     monkeypatch.setattr('your_module.connect_to_mssql', mock_connect_to_mssql)
#     monkeypatch.setattr('your_module.connect_to_db2', mock_connect_to_db2)
#
#     # Run the clean_up function
#     clean_up()
#
#     # Add your assertions here to validate the behavior of clean_up
#     # For example, you can assert that the close method was called on the connections
#     assert mock_connect_to_mssql.called
#     assert mock_connect_to_db2.called
#
# # Run the tests
# if __name__ == '__main__':
#     pytest.main()
from unittest import mock
from src.db_wrapper import clean_up

# @mock.patch('clean_up')
# def test_mock(mocker):
#     mocker.return_value = None
#     clean_up()
#
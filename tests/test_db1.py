import unittest
from unittest import mock
from unittest.mock import patch, MagicMock

from src.db1 import connect_to_db2, _execute_db2_query
from src.db2 import _run_mssql_stored_procedure, update_traces_and_status_of_load_ids
from src.db_wrapper import clean_up


@mock.patch('ibm_db.connect')
def test_connect_to_db2(config_and_resources_manager, mock_connect=None):
    mock_connect.return_value = 'mocked connection'
    conn = connect_to_db2(config_and_resources_manager)

    assert conn == 'mocked connection'


# Assuming you have a test function for _execute_db2_query

def test_execute_db2_query(conn=None):
    with unittest.mock.patch('ibm_db.cursor') as mock_cursor:
        # Create a mock cursor object
        mock_cursor_instance = mock_cursor.return_value

        # Set the expected return value of fetchall()
        expected_result = [('data1', 1), ('data2', 2)]
        mock_cursor_instance.fetchall.return_value = expected_result

        # Call the function you want to test
        result = _execute_db2_query(conn, 'SELECT * FROM table')

        # Assertions
        assert result == expected_result
        mock_cursor.assert_called_once()
        mock_cursor_instance.execute.assert_called_once_with('SELECT * FROM table', None)
        mock_cursor_instance.fetchall.assert_called_once()  # Ensure fetchall was called


def test_run_mssql_stored_procedure():
    # Create a mock for pyodbc.Connection
    mssql_connection_mock = mock.MagicMock()
    cursor_mock = mssql_connection_mock.cursor.return_value

    # Execute the function with the mocked objects
    query = "SELECT * FROM table"
    params = ("param1", "param2")
    _run_mssql_stored_procedure(mssql_connection_mock, query, params)

    # Assert that the cursor methods are called
    cursor_mock.execute.assert_called_once_with(query, params)
    cursor_mock.commit.assert_called_once()
    cursor_mock.close.assert_called_once()


@mock.patch('src.db2._run_mssql_stored_procedure')
def test_update_traces_and_status_of_load_ids(run_mssql_stored_procedure_mock):
    # Create a mock for pyodbc.Connection
    mssql_connection_mock = mock.MagicMock()

    # Mock the return value of the _run_mssql_stored_procedure function
    run_mssql_stored_procedure_mock.return_value = None

    # Define test data
    load_ids = ['id1', 'id2', 'id3']

    # Call the function with the mocked objects
    update_traces_and_status_of_load_ids(mssql_connection_mock, load_ids)

    # Assert that the _run_mssql_stored_procedure is called with the correct arguments
    run_mssql_stored_procedure_mock.assert_called_once_with(
        mssql_connection_mock,
        "exec sp akhthi",
        ','.join(load_ids)
    )


@mock.patch('src.db1.connect_to_db2')
@mock.patch('src.db2.connect_to_mssql')
def test_clean_up(mock_connect_to_db2, mock_connect_to_mssql):
    # Mock the _db2_conn object
    mock_db2_connect = MagicMock()
    mock_mssql_connect = MagicMock()
    mock_connect_to_db2.return_value = mock_db2_connect
    mock_connect_to_mssql.return_value = mock_mssql_connect
    mock_db2_connect.return_value = None
    mock_mssql_connect.return_value = None




    # Call the clean_up() function
    clean_up()



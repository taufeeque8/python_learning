from unittest import mock, TestCase
import unittest
from src import insertT
from src.db2 import connect_to_db, execute_query


def fix_dbc():
    dbc = mock.MagicMock(spec=['cursor'])
    dbc.autocommit = True
    return dbc
def fix_rows():
        rows = [{'id':1, 'name':'John'},
                {'id':2, 'name':'Jane'},]
        return rows


def test_insert_rows_calls_cursor_method():
    dbc = fix_dbc()
    rows = fix_rows()
    insertT.insert_rows(rows, 'users', dbc)
    TestCase.assertTrue(None,dbc.cursor.called)

@mock.patch("src.db2.ibm_db.connect")
def test_connect_to_db(mocked_connect_to_db):
    mocked_connect_to_db.return_value = True
    assert connect_to_db('database', 'hostname', 'port', 'username', 'password') == True


# def test_execute_query():
#     with unittest.mock.patch('ibm_db.connect') as mock_connect:
#         with unittest.mock.patch('ibm_db.cursor') as mock_cursor:
#             mock_conn_instance = mock_connect.return_value
#             mock_cursor_instance = mock_cursor.return_value
#             expected_result = [('data1', 1), ('data2', 2)]
#             mock_cursor_instance.fetchall.return_value = expected_result
#             result = execute_query(mock_conn_instance, 'SELECT * FROM table')
#             assert result == expected_result
#     # assert  execute_query(conn=dbc,query=None) == "statement"
def test_execute_db2_query_1():
    with unittest.mock.patch('ibm_db.connect') as mock_connect:
        with unittest.mock.patch('ibm_db.cursor') as mock_cursor:
            # Create a mock cursor object
            mock_conn_instance = mock_connect.return_value
            mock_cursor_instance = mock_cursor.return_value

            # Set the expected return value of fetchall()
            expected_result = [('data1', 1), ('data2', 2)]
            mock_cursor_instance.fetchall.return_value = expected_result

            # Call the function you want to test
            result = execute_query(mock_conn_instance, 'SELECT * FROM table')

            # Assertions
            assert result == expected_result


import unittest
from unittest import mock
from unittest.mock import MagicMock, call
from src.db2 import execute_query, get_load_id


class TestDB(unittest.TestCase):
    def test_execute_query(self):
        # Mock the connection object
        conn = MagicMock()

        # Mock the cursor and its methods
        cursor = conn.cursor.return_value
        cursor.fetchall.return_value = [('John', 25), ('Alice', 30)]

        # Define the query to be executed
        query = "SELECT * FROM users"

        # Call the execute_query function
        result = execute_query(conn, query)

        # Assert the expected result
        expected_result = [('John', 25), ('Alice', 30)]
        self.assertEqual(result, expected_result)

        # Assert that the cursor methods were called correctly
        conn.cursor.assert_called_once()
        cursor.execute.assert_called_once_with(query)
        cursor.fetchall.assert_called_once()

        conn.cursor.assert_has_calls([call()])

    @mock.patch('src.db2.execute_query')
    def test_get_load_id(self, mock_execute_query):
        # Mock the execute_query function
        mock_result = [('12345',)]
        mock_execute_query.return_value = mock_result

        # Mock the DB2 connection
        db2_conn_mock = mock.MagicMock()

        # Call the function under test
        solr_file_name = 'example.solr'
        result = get_load_id(db2_conn_mock, solr_file_name)

        # Assert the expected behavior

        self.assertEqual(result, mock_result)


    def test_execute_query(self):
        # Mocking the cursor, execute, and fetchall methods
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor.return_value
        mock_cursor.fetchall.return_value = [('result1',), ('result2',)]

        # Define your test data
        query = 'SELECT * FROM my_table'
        params = ()

        # Call the function under test
        result = execute_query(mock_conn, query, params)

        # Assert that the cursor methods were called as expected
        mock_conn.cursor.assert_called_once()
        mock_cursor.execute.assert_called_once_with(query)
        mock_cursor.fetchall.assert_called_once()

        # Assert the expected result
        expected_result = [('result1',), ('result2',)]
        self.assertEqual(result, expected_result)

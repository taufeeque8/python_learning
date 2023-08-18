import pytest
from unittest import mock
import db2 as db2


@pytest.fixture
def mocked_connect_to_db():
    with mock.patch('db2.connect_to_db') as mock_connect_to_db:
        yield mock_connect_to_db


def test_execute_query(mocked_connect_to_db):
    # Mock the return value of connect_to_db
    mocked_conn = mock.MagicMock()
    mocked_connect_to_db.return_value = mocked_conn

    # Mock the return value of exec_immediate
    mocked_stmt = mock.MagicMock()
    mocked_conn.return_value = mocked_stmt

    # Call the execute_query function
    conn = db2.connect_to_db("database", "hostname", "port", "username", "password")
    stmt = db2.execute_query(conn, "SELECT * FROM table")

    # Assert that the mock functions were called correctly
    mocked_connect_to_db.assert_called_once_with("database", "hostname", "port", "username", "password")
    mocked_conn.assert_called_once_with(conn, "SELECT * FROM table")

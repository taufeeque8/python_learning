import unittest
from unittest import mock
from src.db2 import connect_to_db
import pytest

@mock.patch('ibm_db.connect')
def test_connect_to_db(mock_connect):
    # Mock the return value of ibm_db.connect
    mock_connect.return_value = 'mocked connection'

    # Define the input parameters for the function
    database = 'mydatabase'
    hostname = 'localhost'
    port = '50000'
    username = 'myuser'
    password = 'mypassword'

    # Call the function being tested
    conn = connect_to_db(database, hostname, port, username, password)

    # Verify the mock was called with the correct arguments
    mock_connect.assert_called_once_with(
        "DATABASE=mydatabase;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;",
        '', ''
    )

    assert  conn == 'mocked connection'

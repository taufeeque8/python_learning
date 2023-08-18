import unittest
from unittest.mock import patch, MagicMock
import pyodbc
from src.globals import ConfigAndResourcesManager

def connect_to_mssql(config_and_resources_manager: ConfigAndResourcesManager):
    return pyodbc.connect("select * from abc")

class TestConnectToMssql(unittest.TestCase):

    @patch('pyodbc.connect')
    def test_connect_to_mssql(self, mock_connect):
        # Mock the pyodbc.connect function
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        # Call the function under test
        result = connect_to_mssql(config_and_resources_manager=None)

        # Assertions
        mock_connect.assert_called_with("select * from abc")
        self.assertEqual(result, mock_connection)

if __name__ == '__main__':
    unittest.main()

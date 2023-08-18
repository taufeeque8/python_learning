from typing import List, Tuple
import ibm_db
import unittest.mock

class ConfigAndResourcesManager:
    def get(self, section: str, key: str):
        # Implementation for retrieving configuration values
        pass

def connect_to_db2(config_and_resources_manager: ConfigAndResourcesManager):
    db = config_and_resources_manager.get('DatabaseSection', 'db2_db')
    return ibm_db.db2.connect(db)


def _execute_db2_query(conn, query: str, params=None) -> List[Tuple]:
    cursor = conn.cursor()
    if params is None:
        cursor.execute(query)
    else:
        cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    return result

# Assuming you have a test function for _execute_db2_query
def test_execute_db2_query():
    with unittest.mock.patch('ibm_db.connect') as mock_connect:
        with unittest.mock.patch('ibm_db.cursor') as mock_cursor:
            # Create a mock connection and cursor
            mock_conn_instance = mock_connect.return_value
            mock_cursor_instance = mock_cursor.return_value

            # Set the expected return value of fetchall()
            expected_result = [('data1', 1), ('data2', 2)]
            mock_cursor_instance.fetchall.return_value = expected_result

            # Call the function you want to test
            result = _execute_db2_query(mock_conn_instance, 'SELECT * FROM table')

            # Assertions
            assert result == expected_result
            mock_connect.assert_called_once()  # Ensure connect was called
            mock_cursor.assert_called_once()  # Ensure the cursor was created
            mock_cursor_instance.execute.assert_called_once_with('SELECT * FROM table', None)  # Ensure execute was called with the correct arguments
            mock_cursor_instance.fetchall.assert_called_once()  # Ensure fetchall was called

from unittest.mock import patch, MagicMock


# Assuming you have a function that uses the cursor
def execute_query(cursor):
    # Code that uses the cursor
    result = cursor.fetchall()
    return result

def test_expected_query():
    # Mocking the cursor class
    with patch('ibm_db.cursor') as mock_cursor:
        # Creating a mock cursor object
        mock_cursor_instance = mock_cursor.return_value

        # Mocking the fetchall method
        mock_fetchall = MagicMock(return_value=[('data1', 1), ('data2', 2)])
        mock_cursor_instance.fetchall = mock_fetchall

        # Calling the function under test
        result = execute_query(mock_cursor_instance)

        # Assertions
        assert result == [('data1', 1), ('data2', 2)]
        mock_fetchall.assert_called_once()

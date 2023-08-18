import unittest
import sqlite3
class TestDatabaseConnection(unittest.TestCase):
    def test_database_connection(self):
        # Create a database connection
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        # Execute a simple query
        cursor.execute("SELECT 1")
        # Fetch the result
        result = cursor.fetchone()
        # Close the database connection
        cursor.close()
        conn.close()
        # Assert that the result is as expected
        self.assertEqual(result, (1,))
if __name__ == '__main__':
    unittest.main()

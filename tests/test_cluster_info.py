import unittest
from src.ClusterInfo import ClusterInfo

class TestClusterInfo(unittest.TestCase):
    def setUp(self):
        # Create an instance of ClusterInfo with sample data for testing
        self.cluster_info = ClusterInfo("ACTIVE", 1, "properties.json")

    def test_is_active(self):
        self.assertTrue(self.cluster_info.is_active)

    def test_is_inactive(self):
        self.assertFalse(self.cluster_info.is_inactive)

    def tearDown(self):
       self.cluster_info = None

if __name__ == '__main__':
    unittest.main()

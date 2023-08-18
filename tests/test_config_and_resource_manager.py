# import unittest
# from unittest import mock
# from src.ConfigAndResourceManager import ConfigAndResourcesManager
#
# class TestConfigAndResourcesManager(unittest.TestCase):
#     def setUp(self):
#         self.manager = ConfigAndResourcesManager()
#
#     def test_read_config_file_resource(self):
#         # Mock the read_text method of pkg_resources
#         with mock.patch('src.ConfigAndResourceManager.pkg_resources.files') as mock_files:
#             # Mock the return value of read_text
#             mock_files.return_value.joinpath.return_value.read_text.return_value = '[Config]\nkey=value'
#
#             # Call the method being tested
#             self.manager.read_config_file_resource('test.ini')
#
#             # Assert that the config value is correctly read
#             self.assertEqual(self.manager.get('Config', 'key'), 'value')
#
#     def test_get_config_value_with_override(self):
#         # Set environment variable for overriding the config value
#         with mock.patch.dict('os.environ', {'CONFIG_Config_item': 'overridden_value'}):
#             # Set an initial config value
#             self.manager.read_config_string('[Config]\nitem=default_value')
#
#             # Call the method being tested
#             result = self.manager.get_config_value('Config', 'item')
#
#             # Assert that the overridden value is returned
#             self.assertEqual(result, 'overridden_value')
#
#     def test_get_contents_of_resource_file(self):
#         # Mock the read_text method of pkg_resources
#         with mock.patch('src.ConfigAndResourceManager.pkg_resources.files') as mock_files:
#             # Mock the return value of read_text
#             mock_files.return_value.joinpath.return_value.read_text.return_value = 'file contents'
#
#             # Call the method being tested
#             result = self.manager.get_contents_of_resource_file('test.txt')
#
#             # Assert that the file contents are correctly returned
#             self.assertEqual(result, 'file contents')
#
#     # Add more test methods as needed
#
# if __name__ == '__main__':
#     unittest.main()
import unittest
from unittest.mock import patch
from io import StringIO
from src import resources
from src.ConfigAndResourceManager import ConfigAndResourcesManager


class ConfigAndResourcesManagerTests(unittest.TestCase):

    def setUp(self):
        self.config_manager = ConfigAndResourcesManager()

    def test_read_config_file_resource(self):
        # Prepare
        resource_file_name = "config.ini"
        expected_config = {
            "Section1": {
                "key1": "value1",
                "key2": "value2"
            },
            "Section2": {
                "key3": "value3"
            }
        }
        # Mock the behavior of pkg_resources to read the resource file
        with patch("pkg_resources.files") as mock_files:
            mock_resource_file = mock_files.return_value.joinpath.return_value
            mock_resource_file.read_text.return_value = self._config_to_string(expected_config)

            # Act
            self.config_manager.read_config_file_resource(resource_file_name)

            # Assert
            self.assertEqual(self.config_manager._config_parser.sections(), expected_config.keys())
            for section, values in expected_config.items():
                for key, value in values.items():
                    self.assertEqual(self.config_manager._config_parser.get(section, key), value)


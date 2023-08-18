import os
import unittest
from unittest.mock import patch

from src.files_db import get_doctype_and_paths

class TestGetDoctypeAndPaths(unittest.TestCase):

    def setUp(self):
        self.folder_mapping = ("doc_type", "input", "temp", "processed", "error")
        self.input_folder = "/path/to/input"
        self.temp_folder = "/path/to/temp"
        self.processed_folder = "/path/to/processed"
        self.error_folder = "/path/to/error"
        self.secondary_location = "/path/to/secondary"

    def test_get_doctype_and_paths_with_secondary_location(self):
        expected_result = (
            "doc_type",
            os.path.join(self.input_folder, self.folder_mapping[1]),
            os.path.join(self.temp_folder, self.folder_mapping[2]),
            os.path.join(self.processed_folder, self.folder_mapping[3]),
            os.path.join(self.error_folder, self.folder_mapping[4]),
            os.path.join(self.secondary_location, self.folder_mapping[1])
        )

        with patch("os.path.join") as mock_join:
            mock_join.side_effect = lambda *args: "/".join(args)

            result = get_doctype_and_paths(
                self.folder_mapping,
                self.input_folder,
                self.temp_folder,
                self.processed_folder,
                self.error_folder,
                self.secondary_location
            )

        self.assertEqual(result, expected_result)
        mock_join.assert_has_calls([
            mock_join(self.input_folder, self.folder_mapping[1]),
            mock_join(self.temp_folder, self.folder_mapping[2]),
            mock_join(self.processed_folder, self.folder_mapping[3]),
            mock_join(self.error_folder, self.folder_mapping[4]),
            mock_join(self.secondary_location, self.folder_mapping[1])
        ])

    def test_get_doctype_and_paths_without_secondary_location(self):
        expected_result = (
            "doc_type",
            os.path.join(self.input_folder, self.folder_mapping[1]),
            os.path.join(self.temp_folder, self.folder_mapping[2]),
            os.path.join(self.processed_folder, self.folder_mapping[3]),
            os.path.join(self.error_folder, self.folder_mapping[4]),
            None
        )

        with patch("os.path.join") as mock_join:
            mock_join.side_effect = lambda *args: "/".join(args)

            result = get_doctype_and_paths(
                self.folder_mapping,
                self.input_folder,
                self.temp_folder,
                self.processed_folder,
                self.error_folder,
                None
            )

        self.assertEqual(result, expected_result)
        mock_join.assert_has_calls([
            mock_join(self.input_folder, self.folder_mapping[1]),
            mock_join(self.temp_folder, self.folder_mapping[2]),
            mock_join(self.processed_folder, self.folder_mapping[3]),
            mock_join(self.error_folder, self.folder_mapping[4])
        ])

if __name__ == "__main__":
    unittest.main()

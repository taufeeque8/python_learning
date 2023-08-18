import io
import unittest
from typing import Dict
from unittest.mock import mock_open, patch

from src.adshk import _generate_config_file_with_params, generate_config_file


class TestConfigFileGeneration(unittest.TestCase):

    def test__generate_config_file_with_params(self):
        output_path = 'output.txt'
        template_str = "Hello, <NAME>!"
        params = {'<NAME>': 'John Doe'}

        expected_output = "Hello, John Doe!\n"

        with patch('builtins.open', mock_open()) as mock_file:
            _generate_config_file_with_params(output_path, template_str, params)

            mock_file.assert_called_once_with(output_path, 'w', encoding='utf-8', newline='\n')
            handle = mock_file()
            handle.write.assert_called_once_with(expected_output)

    def test_generate_config_file(self):
        output_path = 'output.txt'
        template_str = "Hello, <NAME>!"
        collection_name = "my_collection"
        hdfs_path = "/path/to/hdfs"
        solr_batch_size = 10000
        num_exec = 10
        exec_men = "10g"
        exec_core = 3
        mail_recipients = "sdp_core_dev, search-coe-dev"

        expected_params = {
            '<SOLR_COLLECTION>': collection_name,
            '<HDFSPATH>': hdfs_path,
            '<SOLR BATCH SIZE>': str(solr_batch_size),
            '<NUM EXEC>': str(num_exec),
            '<EXEC_NEM>': exec_men,
            '<EXEC_CORE>': str(exec_core),
            '<MAIL RECIPIENTS>': mail_recipients,
        }

        with patch('builtins.open', mock_open()) as mock_file:
            generate_config_file(output_path, template_str, collection_name, hdfs_path,
                                 solr_batch_size=solr_batch_size, num_exec=num_exec, exec_men=exec_men,
                                 exec_core=exec_core, mail_recipients=mail_recipients)

            mock_file.assert_called_once_with(output_path, 'w', encoding='utf-8', newline='\n')
            handle = mock_file()
            handle.write.assert_called_once()

            # _generate_config_file_with_params.assert_called_once_with(output_path, template_str, expected_params)


if __name__ == '__main__':
    unittest.main()

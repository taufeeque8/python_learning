from unittest.mock import patch, Mock
from src.my import main


@patch("src.my.util", Mock(return_value="dummy"))
@patch("src.my.get_data", Mock(return_value="some data"))
def test_main():
    result = main()
    assert result =='dummy'

@patch("src.my.util")
@patch("src.my.get_data")
def test_main_util_called_with_expected_parameter(get_data_mock, util_mock):
    get_data_mock.return_value = 'some data'
    util_mock.return_value = 'dummy'
    result = main()
    assert result =='dummy'
    util_mock.assert_any_call('some data')
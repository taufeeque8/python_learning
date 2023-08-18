from unittest import mock
from src.sample import random_sum

@mock.patch("src.sample.random.randint")
def test_random_sum(mock_randint):
    mock_randint.return_value = 3
    assert random_sum() == 6

import json
from unittest.mock import mock_open, patch

import pytest

from scripts.build_inverted_index import build_inverted_indexes, write_inverted_indexes


@pytest.fixture
def word_indexes():
    return {
        "cowboy": ["cowboy.txt", "cowboy2.txt", "cowboy3.txt"],
        "cabaret": ["cowboy.txt", "cowboy2.txt", "cowboy3.txt"],
        "1931": ["cowboy.txt", "cowboy2.txt", "cowboy3.txt"],
        "mannie": ["cowboy.txt", "cowboy2.txt", "cowboy3.txt"],
        "davis": ["cowboy.txt", "cowboy2.txt", "cowboy3.txt"],
        "john": ["cowboy.txt", "cowboy2.txt", "cowboy3.txt"],
        "foster": ["cowboy.txt", "cowboy2.txt", "cowboy3.txt"],
    }


@patch("os.listdir")
def test_build_inverted_indexes(listdir_mock, word_indexes):
    file_content = "cowboy cabaret 1931  mannie davis john foster"
    filenames_list = ["cowboy.txt", "cowboy2.txt", "cowboy3.txt"]
    mock = mock_open(read_data=file_content)
    listdir_mock.return_value = filenames_list
    expected_indexes = word_indexes

    with patch("builtins.open", mock):
        inverted_indexes = build_inverted_indexes("some_file")

    assert inverted_indexes == expected_indexes


@patch("builtins.open", new_callable=mock_open)
def test_write_inverted_indexes(mock_open_file, word_indexes):
    write_inverted_indexes(word_indexes)
    mock_file_handle = mock_open_file()

    mock_file_handle.write.assert_called_with(json.dumps(word_indexes))

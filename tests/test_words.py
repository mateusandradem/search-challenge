from unittest.mock import mock_open, patch

import pytest

from src.words import search_words


@pytest.fixture
def json_indexed_words():
    return """
    {
        "walt": ["cowboy.txt", "alice.txt", "alpine.txt"],
        "disney": ["cowboy.txt", "alice.txt"]
    }
    """


@pytest.mark.parametrize(
    "words,expected_matches",
    [
        (["walt", "disney"], ["alice.txt", "cowboy.txt"]),
        (["luiza", "labs"], []),
        (["walt"], ["alice.txt", "alpine.txt", "cowboy.txt"]),
    ],
)
def test_search_words(json_indexed_words, words, expected_matches):
    mock = mock_open(read_data=json_indexed_words)

    with patch("builtins.open", mock):
        matches = search_words(words)

    assert matches == expected_matches

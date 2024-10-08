from unittest.mock import mock_open, patch

import pytest

from search.words import search_words


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

import pytest


@pytest.fixture
def json_indexed_words():
    return """
    {
        "walt": ["cowboy.txt", "alice.txt", "alpine.txt"],
        "disney": ["cowboy.txt", "alice.txt"]
    }
    """

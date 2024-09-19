import json


def search_words(words: list[str]) -> set[str]:
    with open("processed_word_indexes.json") as file:
        indexes = json.loads(file.read())

    matches = {}
    for word in words:
        try:
            matches[word] = set(indexes[word])
        except KeyError:
            matches[word] = set()

    matches_filenames = matches[words[0]]

    for word in matches:
        matches_filenames &= matches[word]

    return sorted(matches_filenames)

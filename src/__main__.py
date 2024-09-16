import sys
import json
from collections import defaultdict

MAX_INT = 2**32


def search_words(words: str) -> dict[str, list[str]]:
    with open("processed_word_indexes.json") as file:
        indexes = json.loads(file.read())

    words_matches = defaultdict(set)
    for word in words:
        try:
            for word_match in indexes[word]:
                words_matches[word].add(word_match)
        except KeyError:
            words_matches[word] = set()

    matches_filenames = words_matches[words[0]]
    for word in words_matches:
        matches_filenames &= words_matches[word]

    matches_number = 0
    breakpoint()
    for filename in matches_filenames:
        min_matches = MAX_INT
        for word in words:
            min_matches = min(min_matches, indexes[word][filename])

        matches_number += min_matches

    return matches_number, matches_filenames

def main():
    if len(sys.argv) < 2:
        print("Fonrneça ao menos 1 palavra")
        sys.exit(1)

    words = sys.argv[1:]
    matches_number, filenames = search_words(words)

    print(f'Foram encontradas {matches_number} ocorrências pelo termo "{" ".join(words)}".')
    print(f'Os arquivos que possuem "{" ".join(words)}" são:')
    print(f'{"\n".join(filenames)}')

if __name__ == "__main__":
    main()

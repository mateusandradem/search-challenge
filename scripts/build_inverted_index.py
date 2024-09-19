import json
import os
from collections import defaultdict


def build_inverted_indexes(dir_name: str) -> defaultdict[list]:
    indexes = defaultdict(list)

    for filename in sorted(os.listdir(dir_name)):
        file_path = os.path.join(dir_name, filename)

        with open(file_path, "r") as movie_file:
            lines = movie_file.readlines()
            for line in lines:
                words = set(line.split())
                for word in words:
                    indexes[word].append(filename)

    return indexes


def write_inverted_indexes(indexes: dict[str]):
    with open("processed_word_indexes.json", "w") as word_file:
        indexes_json = json.dumps(indexes)
        word_file.write(indexes_json)


if __name__ == "__main__":
    write_inverted_indexes(build_inverted_indexes("data"))

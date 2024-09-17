import json
import os
from collections import defaultdict

indexes = defaultdict(list)

for filename in sorted(os.listdir("data")):
    file_path = os.path.join("data", filename)

    with open(file_path, "r") as movie_file:
        lines = movie_file.readlines()
        for line in lines:
            words = set(line.split())
            for word in words:
                indexes[word].append(filename)


with open("processed_word_indexes.json", "w") as word_file:
    indexes_json = json.dumps(indexes)
    word_file.write(indexes_json)

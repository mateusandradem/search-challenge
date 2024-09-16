import os
import json
from collections import Counter, defaultdict


indexes = defaultdict(dict)

for filename in sorted(os.listdir("data")):
    file_path = os.path.join("data", filename)

    with open(file_path, "r", encoding="utf-8") as movie_file:
        lines = movie_file.readlines()
        for line in lines:
            counter = Counter(line.split())
            for word in counter:
                indexes[word].update({file_path: counter[word]})


with open("processed_word_indexes.json", "w") as word_file:
    indexes_json = json.dumps(indexes)
    word_file.write(indexes_json)


# Search challenge

![search-challenge-workflow](https://github.com/mateusandradem/search-challenge/actions/workflows/build.pipeline.yaml/badge.svg)

This repository contains a project to Luizalabs search challenge.

## Requirements

The project requires [Python 3.12](https://www.python.org/downloads/release/python-3120/) or higher and the [Poetry](https://python-poetry.org/) package manager.

## Instalation

After install all requirements, install the project running:
```console
poetry install --with lint,tests
```
## Tests

Run the tests with:
```console
poetry run pytest
```

## Run the application

First, it is necessary to generate the file with the word indexes, run:
```console
poetry run python search/scripts/build_inverted_index.py
```

This script will generate a file called `processed_word_indexes.json`.

P.S: This file and the movies `data` directory needs to be where you run the script and the project, preferably in the root.

So, run the project locally with:
```console
poetry run python search [words]
```


import sys

from words import search_words


def main():
    if len(sys.argv) < 2:
        print("Fonrneça ao menos 1 palavra")
        sys.exit(1)

    words = sys.argv[1:]
    matches = search_words(words)

    print(f'Foram encontradas {len(matches)} ocorrências pelo termo "{" ".join(words)}".')
    print(f'Os arquivos que possuem "{" ".join(words)}" são:')
    print(f'{"\n".join(matches)}')


if __name__ == "__main__":
    main()

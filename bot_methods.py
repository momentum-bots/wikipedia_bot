import wikipedia


def search(text):
    print(wikipedia.search(text))


if __name__ == '__main__':
    search('text')
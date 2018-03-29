import wikipedia


WIKI_PHOTO = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEaF0CsI_3jjaTkV1Cv3f-WD4evU8EFuqcTUH8_-Fpcrkwo57kQA'


def search(text):
    print(wikipedia.search(text))


def get_photo_url(article, lang):
    wikipedia.set_lang(lang)
    try:
        page = wikipedia.page(article)
        images = [image for image in page.images if 'jpg' in image]
        if images:
            return images[0]
    except Exception as e:
        print('[Exception] {}'.format(e))
    return WIKI_PHOTO


if __name__ == '__main__':
    search('text')

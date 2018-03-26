import wikipedia
from telebot import types
import bot_methods
import datetime
import generate_telegraph
import users_controller
import requests
from bs4 import BeautifulSoup


WIKI_PHOTO = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEaF0CsI_3jjaTkV1Cv3f-WD4evU8EFuqcTUH8_-Fpcrkwo57kQA'


def parse_article(url):
    page = requests.get(url)
    html = page.text

    title = url.split('/')[-1].replace('_', ' ')

    soup = BeautifulSoup(html, 'lxml')
    body_content = soup.find('div', class_='mw-parser-output')
    return body_content, title


def parse_main_photo(article=None, body_content=None, lang=None):

    if article:
        url = 'https://{}.wikipedia.org/wiki/'.format(lang) + article.replace(' ', '_')
        body_content, title = parse_article(url)
    try:
        main_photo = body_content.find('table', class_='infobox').find('a', class_='image').find('img')['src']
        img_src = 'https:' + main_photo
        return img_src
    except:
        print('no main photo')
        return None


def get_photo_url(article, lang):
    main_photo_url = parse_main_photo(article=article, lang=lang)
    if main_photo_url:
        print('yep')
        return main_photo_url

    wikipedia.set_lang(lang)
    try:
        page = wikipedia.page(article)
        images = [image for image in page.images if 'jpg' in image]
        if images:
            return images[0]
    except:
        pass
    return WIKI_PHOTO




def add_button(article, i, lang, queue):
    queue.put(types.InlineQueryResultArticle(
                   id=str(i), title=article,
                   #description='test',
                   input_message_content=types.InputTextMessageContent(article),
                   thumb_url=get_photo_url(article, lang),
                   thumb_width=48,
                   thumb_height=48
    ))
    print('finished at:{}'.format(datetime.datetime.now()))

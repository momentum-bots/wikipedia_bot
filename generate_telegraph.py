import wikipedia
from bs4 import BeautifulSoup
from telegraph import Telegraph, TelegraphException
from config import TELEGRAPH_TOKEN
import lxml
import bot_methods
from languages import LANGUAGES_DICTIONARY


WIKI_URL = 'https://en.wikipedia.org'


def make_pretty(content):
    new_content = BeautifulSoup(content, 'lxml').prettify()
    start_tags = ['<html>', '<head>', '<body>', '<tt>']
    end_tags = [tag[0] + '/' + tag[1:] for tag in start_tags]

    for tag in start_tags + end_tags:
        new_content = new_content.replace(tag, ' ')
    return new_content


def create_instant_view(content, title, bot, uid, too_big=False) :
    telegraph = Telegraph(TELEGRAPH_TOKEN)
    bot.send_chat_action(uid, 'typing')

    try :
        response = telegraph.create_page(title=title, html_content=content)
        return response['url']  # url of created telegraph page

    except TelegraphException:
        new_content = "<h".join(content.split('<h')[:-1]) + "<br></br><aside>Сделано ботом <br></br><a href ='https://telegram.me/WikipediaTelegraphBot?start=from_telegraph'> @WikipediaTelegraphBot</a></aside>"
        print('too big article')
        return create_instant_view(make_pretty(new_content), title, bot, uid, too_big=True)


def generate_by_wiki_url(url, lang, bot, uid):
    body_content, title = bot_methods.parse_article(url)

    content = ''
    img_url = bot_methods.parse_main_photo(body_content=body_content)
    if img_url is not None:
        content += "<img src='{}'></img>".format(img_url)

    for child in body_content.children:
        if child.name is not None:

            if child.name == 'dl':
                try:
                    urls = child.find_all('img', class_='mwe-math-fallback-image-inline')
                    for url in urls:
                        content += "<img src='{}'></img>".format(url['src'])
                        print(url['src'])
                except:
                    print('ne vyshlo')

            #headers, telegraph supports only <h3> and <h4> header tags
            if child.name in ['h2', 'h3', 'h4']:
                header = child.get_text().split('[')[0]
                if child.name == 'h2':
                    content += '<h3>{}</h3>'.format(header)
                elif child.name == 'h3':
                    content += '<h4>{}</h4>'.format(header)
                elif child.name == 'h4':
                    content += '<h4><em>{}</em></h4>'.format(header)

            #paragraphs
            elif child.name == 'p':
                childs = []
                for p_child in child.children:
                    childs.append(p_child.name)

                if len(childs) == 2 and child.find('img', class_='mwe-math-fallback-image-inline'):
                    # print(p_child)
                    url = child.find('img', class_='mwe-math-fallback-image-inline')
                    if url is not None:
                        content += "<img src='{}'></img>".format(url['src'])
                else:
                    p = ''
                    for p_child in child.children:
                        if p_child.name in ['sup', 'span', 'tt']:
                            if p_child.find('img', class_='mwe-math-fallback-image-inline'):
                                url = p_child.find('img', class_='mwe-math-fallback-image-inline')['src']
                                p += "[<a href='{}'>{}</a>]".format(url, LANGUAGES_DICTIONARY['formula'][lang])
                            else:
                                p += p_child.get_text().replace('<' , '&lt;').replace('>', '&gt;')
                        else:
                            if p_child.name == 'a':
                                p += "[<a href='{}'>{}</a>]".format(WIKI_URL + p_child['href'], p_child.get_text().replace('<' , '&lt;').replace('>', '&gt;'))
                            else:
                                try:
                                    p += p_child.string.replace('<' , '&lt;').replace('>', '&gt;')
                                except:
                                    print(p_child.string)
                    content += '<p>{}</p>'.format(p)


            #lists
            elif child.name in ['ul', 'ol']:
                content += '<{}>'.format(child.name)
                for li in child.children:
                    li_text = ''
                    if li.string is not None:
                        content += '<li>{}</li>'.format(li.string)
                    else:
                        for part in li.children:
                            if part.string is not None:
                                li_text += part.string
                        content += '<li>{}</li>'.format(li_text.replace('<', '< '))
                content += '</{}>'.format(child.name)

            #blockquotes
            elif child.name == 'blockquote':
                content += '<blockquote>{}</blockquote>'.format(child.get_text())

            elif child.name == 'div':
                if 'class' in child.attrs.keys():
                    #code section
                    if ''.join(child['class']) == 'mw-highlightmw-content-ltr':
                        content += '<pre>{}</pre><br></br>'.format(child.get_text())

                    #images
                    elif child['class'] in [['thumb', 'tright'], ['thumb', 'tleft']]:
                        try:
                            img_src = 'https:' + child.find('img')['src']
                            caption = child.find('div', class_='thumbcaption')

                            thumbcaption = ''
                            if caption.find('img', class_='mwe-math-fallback-image-inline'):
                                for capt_child in caption.children:
                                    try:
                                        url = capt_child.find('img', class_='mwe-math-fallback-image-inline')['src']
                                        thumbcaption += "[<a href='{}'>{}</a>]".format(url, LANGUAGES_DICTIONARY['formula'][lang])
                                    except:
                                        if 'div' not in capt_child and capt_child.string:
                                            thumbcaption += capt_child.string
                            else:
                                thumbcaption += caption.get_text()

                            content += '<figure><img src={}></img><figcaption>{}</figcaption></figure>'.format(img_src, thumbcaption)
                        except:
                            print('no image')


    content += "<hr></hr><aside>{} <br></br><a href ='https://telegram.me/WikipediaTelegraphBot?start=from_telegraph'> @WikipediaTelegraphBot</a></aside>"\
                .format(LANGUAGES_DICTIONARY['created_by'][lang])

    if '<pre>' in content:
        content = bot_methods.make_code_pretty(content)

    new_content = make_pretty(content)

    return create_instant_view(new_content, title, bot, uid)

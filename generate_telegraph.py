import wikipedia
import requests
from bs4 import BeautifulSoup
from telegraph import Telegraph, TelegraphException
from config import TELEGRAPH_TOKEN
import lxml

WIKI_URL = 'https://en.wikipedia.org'


def make_pretty(content):
    new_content = BeautifulSoup(content, 'lxml').prettify()
    start_tags = ['<html>', '<head>', '<body>', '<tt>']
    end_tags = [tag[0] + '/' + tag[1:] for tag in start_tags]

    for tag in start_tags + end_tags:
        new_content = new_content.replace(tag, ' ')
    return new_content


def create_instant_view(content, title) :
    telegraph = Telegraph(TELEGRAPH_TOKEN)

    try :
        response = telegraph.create_page(title=title, html_content=content)
        return response['url']  # url of created telegraph page

    except TelegraphException :
        new_content = "<h".join(content.split('<h')[:-1])
        print('too big article')
        return create_instant_view(make_pretty(new_content), title)


def generate_by_wiki_url(url):
    page = requests.get(url)
    html = page.text

    title = url.split('/')[-1].replace('_', ' ')
    content = ''

    soup = BeautifulSoup(html, 'lxml')
    body_content = soup.find('div', class_='mw-parser-output')

    try:
        main_photo = body_content.find('table', class_='infobox').find('a', class_='image').find('img')['src']
        img_src = 'https://' + main_photo[2:]
        content += "<img src='{}'></img>".format(img_src)
    except:
        pass

    for child in body_content.children:
        if child.name is not None:
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
                content += '<p>{}</p>'.format(child.get_text())
                # for p_child in child.children:
                #     if p_child.name in ['sup', 'span', 'tt']:
                #         p += p_child.get_text()
                #     else:
                #         if p_child.name == 'a':
                #             p += "<a href='{}'>{}</a>".format(WIKI_URL + p_child['href'], p_child.get_text())
                #         else:
                #             p += p_child.string + '&nbsp;'
                #             print(p_child.string + '&nbsp;')
                # print(p, '\n')

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
                            img_src = 'https://' + child.find('img')['src'][2:]
                            caption = child.find('div', class_='thumbcaption').get_text().strip()

                            content += '<figure><img src={}></img><figcaption>{}</figcaption></figure>'.format(img_src, caption)
                        except:
                            print('no image')

    new_content = make_pretty(content)

    with open('content.html', 'w') as f:
        f.write(new_content)

    return create_instant_view(new_content, title)


# print(generate_by_wiki_url('https://en.wikipedia.org/wiki/Cython'))

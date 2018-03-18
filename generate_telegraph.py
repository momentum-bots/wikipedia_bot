import wikipedia
import requests
from bs4 import BeautifulSoup
from telegraph import Telegraph, TelegraphException
from config import TELEGRAPH_TOKEN


def create_instant_view(content, title) :
    telegraph = Telegraph(TELEGRAPH_TOKEN)
    # too_big = False
    # title, content = parse_article(url, title)

    try :
        response = telegraph.create_page(title=title, html_content=content)
        return response['url']  #url of created telegraph page

    except TelegraphException :
        print('too big article')
        pass


#returns url of generated telegraph page
def generate_by_wiki_name(name):
    wikipedia.set_lang('uk')
    page = wikipedia.page(name.replace('_', ' '))

    page_content = page.content

    print(page_content)
    content = ''
    for big_section in page_content.split('\n== ')[1:]:
        section_b = big_section.split(' ==\n')

        big_title = section_b[0]
        big_section_content = section_b[1].split('\n=== ')

        content += '<h3>' + big_title + '</h3>'
        content += '<p>' + big_section_content[0] + '</p>'

        if len(big_section_content) > 1 :
            for medium_section in big_section_content[1:]:
                section_m = medium_section.split(' ===\n')

                medium_title = section_m[0]
                medium_section_content = section_m[1].split('\n==== ')

                content += '<h4>' + medium_title + '</h4>'
                content += '<p>' + medium_section_content[0] + '</p>'

                if len(medium_section_content) > 1:
                    for small_section in medium_section_content[1:]:
                        section_s = small_section.split(' ====\n')

                        small_title = section_s[0]
                        small_section_content = section_s[1]

                        content += '<h4><em>' + small_title + '</em></h4>'
                        content += '<p>' + small_section_content + '</p>'

        return create_instant_view(content, name)


def generate_by_wiki_url(url):
    page = requests.get(url)
    html = page.text

    title = url.split('/')[-1].replace('_', ' ')
    content = ''

    soup = BeautifulSoup(html, 'lxml')
    body_content = soup.find('div', class_='mw-parser-output')

    for child in body_content.children:
        if child.name is not None:
            #headers, telegraph supports only <h3> and <h4> header tags
            if child.name in ['h2', 'h3', 'h4']:
                header = child.get_text().split('[edit]')[0]
                if child.name == 'h2':
                    content += '<h3>{}</h3>'.format(header)
                elif child.name == 'h3':
                    content += '<h4>{}</h4>'.format(header)
                elif child.name == 'h4':
                    content += '<h4><em>{}</em></h4'.format(header)

            #paragraphs
            elif child.name == 'p':
                content += '<p>{}</p>'.format(child.get_text())

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

            if child.name == 'blockquote':
                content += '<blockquote>{}</blockquote>'.format(child.get_text())

            if child.name == 'div' and ''.join(child['class']) == 'mw-highlightmw-content-ltr':
                content += '<pre>{}</pre><br></br>'.format(child.get_text())

    return create_instant_view(content, title)

print(generate_by_wiki_url('https://en.wikipedia.org/wiki/Cython'))

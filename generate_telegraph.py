import wikipedia
from bs4 import BeautifulSoup
import requests
from telegraph import Telegraph, TelegraphException
from config import TELEGRAPH_TOKEN


# def parse_article(url, title, too_big=False) :
#     content = ''
#     page = requests.get(url)
#     html = page.text

#     soup = BeautifulSoup(html, 'lxml')
#     # title = soup.find('h1', class_='entry-title').text.strip()  #title of article
#     # article = soup.find('div', class_='td-post-content')
#     invalid_tags = ['span', 'small', 'html', 'body', 
#                     'head', 'sup', 'strong', 'em', 'div']
#     for tag in invalid_tags: 
#         for match in soup.findAll(tag):
#             match.replaceWithChildren()

#     paragraphs = soup.find_all('p')  #all useful text from article

#     for p in paragraphs:
#         content += str(p)
  
#     return title, content



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
    page = wikipedia.page(name.replace('_', ''))

    page_content = page.content
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
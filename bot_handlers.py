from bot import bot
import wikipedia
import generate_telegraph
import re
from telebot import types
from time import sleep
import users_controller
import keyboards


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    users_controller.add_user(message.chat.id)
    print(message)


@bot.message_handler(commands='set_lang')
def set_lang(message):
    markup = keyboards.create_lang_keyboard()
    bot.send_message(message.chat.id, 'Choose your language:',reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        lang = users_controller.get_lang(message.chat.id)
        url = 'https://{}.wikipedia.org/wiki/'.format(lang) + message.text.replace(' ', '_')
        response = generate_telegraph.generate_by_wiki_url(url)
        bot.send_message(message.chat.id, response)
    except:
        bot.send_message(message.chat.id, 'smth went wrong')


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    user_id = query.from_user.id
    lang = users_controller.get_lang(user_id)
    articles = []
    descriptions = []
    buttons = []

    wikipedia.set_lang(lang)
    for article in wikipedia.search(query.query):
        if 'disambiguation' not in article:
            articles.append(article)

    for i, article in enumerate(articles):
        buttons.append(types.InlineQueryResultArticle(
                       id=str(i), title=article,
                       description='test',
                       input_message_content=types.InputTextMessageContent(article)
        ))
    try:
        bot.answer_inline_query(query.id, buttons)
    except:
        print('fuck')
        return


def start_bot():
    bot.polling(none_stop=True)


if __name__ == '__main__':
        start_bot()

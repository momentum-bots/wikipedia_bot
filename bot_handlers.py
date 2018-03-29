from bot import bot
from telebot import types
import wikipedia
import generate_telegraph
import users_controller
from keyboards import KeyboardManager
import bot_methods
from languages import LANGUAGES_DICTIONARY
from time import sleep


@bot.message_handler(commands=['start'])
def send_welcome(message):
    users_controller.add_user(message.chat.id)
    lang = users_controller.get_lang(message.chat.id)
    bot.send_message(message.chat.id,
                     LANGUAGES_DICTIONARY['greeting'][lang],
                     reply_markup=KeyboardManager.search_keyboard)
    print(message)


@bot.message_handler(commands=['help'])
def help(message):
    users_controller.add_user(message.from_user.id)
    lang = users_controller.get_lang(message.from_user.id)
    bot.send_message(message.chat.id, LANGUAGES_DICTIONARY['help_message'][lang])
    sleep(3)
    bot.send_photo(message.chat.id, open('example1.jpg', 'rb'))
    sleep(1)
    bot.send_photo(message.chat.id, open('example2.jpg', 'rb'))


@bot.message_handler(commands=['set_language'])
def set_lang(message):
    lang = users_controller.get_lang(message.chat.id)
    bot.send_message(message.chat.id, LANGUAGES_DICTIONARY['set_lang'][lang],reply_markup=KeyboardManager.set_lang_keyboard())


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text in LANGUAGES_DICTIONARY['keyboard'].keys():
        users_controller.set_lang(message.chat.id, LANGUAGES_DICTIONARY['keyboard'][message.text])
        lang = users_controller.get_lang(message.chat.id)
        bot.send_message(message.chat.id,
                         LANGUAGES_DICTIONARY['changed_lang'][lang],
                         reply_markup=types.ReplyKeyboardRemove())
    else:
        try:
            lang = users_controller.get_lang(message.from_user.id)
            url = 'https://{}.wikipedia.org/wiki/'.format(lang) + message.text.replace(' ', '_')
            response = generate_telegraph.generate_by_wiki_url(url)
            bot.send_message(message.chat.id, response, reply_markup=KeyboardManager.search_keyboard)
        except Exception as e:
            print('[Exception] {}'.format(e))
            bot.send_message(message.chat.id, 'Server-side error (sorry)', reply_markup=types.ReplyKeyboardRemove())


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    users_controller.add_user(query.from_user.id)
    lang = users_controller.get_lang(query.from_user.id)
    articles = []
    buttons = []

    wikipedia.set_lang(lang)
    for article in wikipedia.search(query.query):
        if 'disambiguation' not in article:
            articles.append(article)

    for i, article in enumerate(articles[:2]):
        buttons.append(types.InlineQueryResultArticle(
                       id=str(i), title=article,
                       description='test',
                       input_message_content=types.InputTextMessageContent(article),
                       thumb_url=bot_methods.get_photo_url(article, lang),
                       thumb_width=48,
                       thumb_height=48)
                       )
    try:
        bot.answer_inline_query(query.id, buttons)
    except Exception as e:
        print('[Exception] {}'.format(e))
        return


def start_bot():
    bot.polling(none_stop=True)


if __name__ == '__main__':
        start_bot()

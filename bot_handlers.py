from bot import bot
import wikipedia
import generate_telegraph
from telebot import types
import users_controller
import keyboards
import bot_methods
from languages import LANGUAGES_DICTIONARY
import threading
from queue import Queue
from time import sleep


@bot.message_handler(commands=['start'])
def send_welcome(message):
    users_controller.add_user(message.from_user.id)
    lang = users_controller.get_lang(message.from_user.id)
    bot.send_message(message.chat.id, LANGUAGES_DICTIONARY['greeting'][lang])
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
    users_controller.add_user(message.from_user.id)
    markup = keyboards.set_lang_keyboard()
    lang = users_controller.get_lang(message.from_user.id)
    bot.send_message(message.from_user.id,
                     LANGUAGES_DICTIONARY['set_lang'][lang],
                     reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    users_controller.add_user(message.from_user.id)
    keyboard_hider = types.ReplyKeyboardRemove()
    if message.text in LANGUAGES_DICTIONARY['keyboard'].keys():
        users_controller.set_lang(message.from_user.id, LANGUAGES_DICTIONARY['keyboard'][message.text])
        lang = users_controller.get_lang(message.from_user.id)
        bot.send_message(message.chat.id,
                         LANGUAGES_DICTIONARY['changed_lang'][lang],
                         reply_markup=keyboard_hider)
    else:
        try:
            lang = users_controller.get_lang(message.from_user.id)
            url = 'https://{}.wikipedia.org/wiki/'.format(lang) + message.text.replace(' ', '_')
            response = generate_telegraph.generate_by_wiki_url(url)
            bot.send_message(message.chat.id, response, reply_markup=keyboard_hider)
        except:
            bot.send_message(message.chat.id, 'Try again..', reply_markup=keyboard_hider)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    users_controller.add_user(query.from_user.id)
    lang = users_controller.get_lang(query.from_user.id)
    articles = []
    descriptions = []
    buttons = []

    wikipedia.set_lang(lang)
    for article in wikipedia.search(query.query):
        if 'disambiguation' not in article:
            articles.append(article)

    queue = Queue()
    threads = []
    print(articles)
    for i, article in enumerate(articles[:5]):
        threads.append(threading.Thread(target=bot_methods.add_button,
                                        args=(article, i, lang, queue)))

    print(threads)
    for thread in threads[:5]:
        thread.start()

    for thread in threads[:5]:
        buttons.append(queue.get())

    try:
        bot.answer_inline_query(query.id, buttons)
    except Exception as e:
        print('[Error] {}'.format(e))
        return


def start_bot():
    bot.polling(none_stop=True)


if __name__ == '__main__':
        start_bot()

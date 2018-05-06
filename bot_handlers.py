from bot import bot
from telebot import types
import wikipedia
import generate_telegraph
import users_controller
from keyboards import KeyboardManager
import bot_methods
from languages import LANGUAGES_DICTIONARY
from time import sleep
import threading
from queue import Queue
from config import BOT_NAME


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        lang = users_controller.get_lang(message.from_user.id)
    except:
        lang = 'en'

    users_controller.add_user(message.from_user.id,
                              username=message.from_user.username,
                              lang=lang)
    text_button = LANGUAGES_DICTIONARY['search'][lang]
    bot.send_message(message.chat.id,
                     LANGUAGES_DICTIONARY['greeting'][lang],
                     reply_markup=KeyboardManager.get_search_keyboard(text_button))
    bot.send_message(message.chat.id,
                     LANGUAGES_DICTIONARY['set_lang'][lang],
                     reply_markup=KeyboardManager.set_lang_keyboard())
    print(message)


@bot.message_handler(commands=['help'])
def help(message):
    try:
        lang = users_controller.get_lang(message.from_user.id)
    except:
        lang = 'en'

    users_controller.add_user(message.from_user.id,
                              username=message.from_user.username,
                              lang=lang)

    bot.send_message(message.chat.id, LANGUAGES_DICTIONARY['help_message'][lang])
    # sleep(3)
    # bot.send_photo(message.chat.id, open('images/example1.jpg', 'rb'))
    # sleep(1)
    # bot.send_photo(message.chat.id, open('images/example2.jpg', 'rb'))


@bot.message_handler(commands=['set_language'])
def set_lang(message):
    try:
        lang = users_controller.get_lang(message.from_user.id)
    except:
        lang = 'en'

    users_controller.add_user(message.from_user.id,
                              username=message.from_user.username,
                              lang=lang)

    bot.send_message(message.from_user.id, LANGUAGES_DICTIONARY['set_lang'][lang],
                     reply_markup=KeyboardManager.set_lang_keyboard())


@bot.message_handler(commands=['rate'])
def send_welcome(message):
    try:
        lang = users_controller.get_lang(message.from_user.id)
    except:
        lang = 'en'
    bot.send_message(message.chat.id, LANGUAGES_DICTIONARY['rate'][lang])


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        lang = users_controller.get_lang(message.from_user.id)
    except:
        lang = 'en'

    users_controller.add_user(message.from_user.id,
                              username=message.from_user.username,
                              lang=lang)

    if message.text in LANGUAGES_DICTIONARY['keyboard'].keys():
        users_controller.set_lang(message.chat.id, LANGUAGES_DICTIONARY['keyboard'][message.text])
        lang = users_controller.get_lang(message.chat.id)
        text_button = LANGUAGES_DICTIONARY['search'][lang]
        del_message = bot.send_message(message.chat.id, '.', reply_markup=types.ReplyKeyboardRemove())
        bot.delete_message(message.chat.id, del_message.message_id)
        bot.send_message(message.chat.id,
                         LANGUAGES_DICTIONARY['changed_lang'][lang],
                         reply_markup=KeyboardManager.get_search_keyboard(text_button))
    else:
        try:
            lang = users_controller.get_lang(message.from_user.id)
            url = 'https://{}.wikipedia.org/wiki/'.format(lang) + message.text.replace(' ', '_')
            bot.send_chat_action(message.chat.id, 'typing')
            response = generate_telegraph.generate_by_wiki_url(url, lang, bot, message.chat.id)
            text_button = LANGUAGES_DICTIONARY['search'][lang]
            bot.send_message(message.chat.id, response, reply_markup=KeyboardManager.get_search_keyboard(text_button))
        except Exception as e:
            print('[Exception] {}'.format(e))
            bot.send_message(message.chat.id, LANGUAGES_DICTIONARY['wrong_article'][lang], reply_markup=types.ReplyKeyboardRemove())


@bot.inline_handler(func=lambda query: len(query.query) == 0)
def query_empty_text(query):
    try:
        lang = users_controller.get_lang(query.from_user.id)
    except:
        lang = 'en'

    users_controller.add_user(query.from_user.id,
                              username=query.from_user.username,
                              lang=lang)

    print('kek')
    r = types.InlineQueryResultArticle(
                id='1',
                title=LANGUAGES_DICTIONARY['hint'][lang],
                description=LANGUAGES_DICTIONARY['hint_desc'][lang],
                input_message_content=types.InputTextMessageContent(
                message_text="🌚🌝")
        )
    bot.answer_inline_query(query.id, [r], cache_time=10)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    try:
        lang = users_controller.get_lang(query.from_user.id)
    except:
        lang = 'en'

    users_controller.add_user(query.from_user.id,
                              username=query.from_user.username,
                              lang=lang)

    articles = []
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
        print('[Exception] {}'.format(e))
        return


def start_bot():
    bot.remove_webhook()
    bot.polling(none_stop=True)


if __name__ == '__main__':
        start_bot()

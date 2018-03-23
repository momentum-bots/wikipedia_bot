from bot import bot
import wikipedia
import generate_telegraph
from telebot import types
import users_controller
import keyboards
import bot_methods
from languages import LANGUAGES_DICTIONARY


@bot.message_handler(commands=['start'])
def send_welcome(message):
    users_controller.add_user(message.chat.id)
    lang = users_controller.get_lang(message.chat.id)
    bot.send_message(message.chat.id, LANGUAGES_DICTIONARY['greeting'][lang])
    print(message)


@bot.message_handler(commands=['set_lang'])
def set_lang(message):
    markup = keyboards.set_lang_keyboard()
    lang = users_controller.get_lang(message.chat.id)
    bot.send_message(message.chat.id, LANGUAGES_DICTIONARY['set_lang'][lang],reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    keyboard_hider = types.ReplyKeyboardRemove()
    if message.text in LANGUAGES_DICTIONARY['keyboard'].keys():
        users_controller.set_lang(message.chat.id, LANGUAGES_DICTIONARY['keyboard'][message.text])
        lang = users_controller.get_lang(message.chat.id)
        bot.send_message(message.chat.id, LANGUAGES_DICTIONARY['changed_lang'][lang], reply_markup=keyboard_hider)
    else:
        try:
            lang = users_controller.get_lang(message.chat.id)
            url = 'https://{}.wikipedia.org/wiki/'.format(lang) + message.text.replace(' ', '_')
            response = generate_telegraph.generate_by_wiki_url(url)
            bot.send_message(message.chat.id, response, reply_markup=keyboard_hider)
        except:
            bot.send_message(message.chat.id, 'smth went wrong', reply_markup=keyboard_hider)


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

    for i, article in enumerate(articles[:2]):
        buttons.append(types.InlineQueryResultArticle(
                       id=str(i), title=article,
                       description='test',
                       input_message_content=types.InputTextMessageContent(article),
                       thumb_url=bot_methods.get_photo_url(article, lang),
                       thumb_width=48,
                       thumb_height=48
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

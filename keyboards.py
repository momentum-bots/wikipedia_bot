from telebot import types
from languages import LANGUAGES_DICTIONARY


class KeyboardManager(object):

    search_keyboard = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text="Search wiki article", switch_inline_query_current_chat="")
    search_keyboard.add(switch_button)

    @staticmethod
    def create_articles_keyboard(language: str, articles: list):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        for article in articles:
            keyboard.add(types.KeyboardButton(article))
        keyboard.add(types.KeyboardButton(LANGUAGES_DICTIONARY[language]['back']))
        return keyboard

    @staticmethod
    def set_lang_keyboard():
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton('🇬🇧 English'))
        keyboard.add(types.KeyboardButton('🇺🇦 Українська'))
        keyboard.add(types.KeyboardButton('🇷🇺 Русский'))
        return keyboard

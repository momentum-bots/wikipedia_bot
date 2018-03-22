from telebot import types
from languages import LANGUAGES_DICTIONARY


def create_articles_keyboard(language: str, articles: list):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for article in articles:
        keyboard.add(types.KeyboardButton(article))
    keyboard.add(types.KeyboardButton(LANGUAGES_DICTIONARY[language]['back']))
    return keyboard


def set_lang_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(types.KeyboardButton('🇬🇧 English'))
    keyboard.add(types.KeyboardButton('🇺🇦 Українська'))
    keyboard.add(types.KeyboardButton('🇷🇺 Русский'))
    return keyboard

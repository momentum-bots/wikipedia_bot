LANGUAGES_DICTIONARY = {
    'keyboard': {'🇬🇧 English': 'en',
                 '🇺🇦 Українська': 'uk',
                 '🇷🇺 Русский': 'ru'
                },
    'greeting': {'en': 'Hi!', 'uk': 'Привіт!', 'ru': 'Привет!'},
    'changed_lang': {'en': 'Language was successfully updated.',
                     'uk': 'Мова була успішно оновлена.',
                     'ru': 'Язык был успешно обновлен.'
                    },
    'wrong_article': {'en': "There's no such article in Wikipedia.. Try again!",
                      'uk': 'У Вікіпедії немає такої статті. Спробуй знову!',
                      'ru': 'В Википедии нет такой статьи. Попробуй снова!'
                     },
    'set_lang': {'en': 'Choose your language:',
                 'uk': 'Виберіть мову:',
                 'ru': 'Выберите язык:'
                }
}


help_message = """This bot can work in your chats and groups, you just need to add it there. Then type @WikipediaTelegraphBot in any chat with your query. This will open a panel with Wikipedia article suggestions. Tap on an item and bot will generate Telegraph page for you!

You can change language of articles anytime  by sending /set_lang command to bot."""

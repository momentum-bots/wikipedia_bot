help_message = """This bot can work in your chats, you just need to add it there as new member. Then call bot by typing its nickname: @WikipediaTelegraphBot in any chat with your query. This will open a panel with Wikipedia article suggestions. Tap on an item and bot will generate Telegraph page for you!

You can change language of articles anytime  by sending /set_language command to bot."""
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
                },
    'help_message': {'en': """This bot can work in your chats, you just need to add it there as new member. Then call bot by typing its nickname: @WikipediaTelegraphBot in any chat with your query. This will open a panel with Wikipedia article suggestions. Tap on an item and bot will generate Telegraph page for you!

You can change language of articles anytime  by sending /set_language command to bot.""",
                     'uk': """Даний бот може працювати у Ваших чатах, Вам всього лише потрібно додати його в них як нового учасника. Далі викликаєте бота, вводячи його нік: @WikipediaTelegraphBot, ставите пробіл і запит з текстом, що Вас цікавить. Бот відповість на цей запит у вигляді випливаючих підказок з назвою вікі-статті. Якщо одна з підказок саме те, що Ви шукали, натискайте на неї і бот згенерує для Вас бажану Телеграф-сторінку, яку можна зручно переглянути у Instant View режимі!

Ви можете змінити мову статей у будь-який момент, надіславши боту команду /set_language.""",
                     'ru': """Этот бот может работать как и лично в Вашей переписке с ним, так и в Ваших чатах. Вам всего лишь нужно добавить его в них как нового участника. Далее вызываете бота, введя его ник:  @WikipediaTelegraphBot, ставите пробел и запрос с текстом, что вас интересует. Бот ответит на этот запрос в виде всплывающих подсказок с названием вики-статьи. Если одна из подсказок именно то, что Вы искали, нажимайте на неё и бот сгенерирует для Вас желаемую Телеграф-страницу, которую можно удобно просмотреть в Instant View режиме!

Вы можете изменить язык статей в любой момент, отправив боту комманду /set_language."""
                    }
}

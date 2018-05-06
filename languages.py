from config import BOT_NAME


LANGUAGES_DICTIONARY = {
    'keyboard': {'🇬🇧 English': 'en',
                 '🇺🇦 Українська': 'uk',
                 '🇷🇺 Русский': 'ru',
                 '🇹🇷 Türkçe': 'tr'
                },
    'greeting': {'en': 'Hi!', 'uk': 'Привіт!', 'ru': 'Привет!', 'tr': 'Merhaba!' },
    'changed_lang': {'en': 'Language was successfully updated.',
                     'uk': 'Мова була успішно оновлена.',
                     'ru': 'Язык был успешно обновлен.',
                     'tr': 'Dil başarıyla güncellendi'
                    },
    'wrong_article': {'en': "There's no such article in Wikipedia.. Try again!",
                      'uk': 'У Вікіпедії немає такої статті. Спробуй знову!',
                      'ru': 'В Википедии нет такой статьи. Попробуй снова!',
                      'tr': 'Vilipedi’de böyle bir makale yok.. Tekrar deneyin'
                     },
    'set_lang': {'en': 'Choose your language: \n(you can change it any time sending /set_language)',
                 'uk': 'Виберіть мову: \n(її можна змінити у будь-який момент, надіславши /set_language)',
                 'ru': 'Выберите язык: \n(его можно изменить в любой момент, отправив /set_language)',
                 'tr': 'Dilinizi seçin: (Dili istediğiniz zaman /set_language komutu göndererek değiştirebilirsiniz)'
                },
    'wrong_article': {'en': 'There is no such article. Try again 🤔',
                      'uk': 'Немає такої статті. Спробуй знову 🤔',
                      'ru': 'Такой статьи нет. Попробуй снова 🤔',
                      'tr': 'Böyle bir makale yok. Tekrar deneyin'
                     },
    'created_by': {'en': 'Created by',
                   'uk': 'Зроблено ботом',
                   'ru': 'Сделано ботом',
                   'tr': 'Oluşturan'
                  },
    'search': {'en': 'Search',
               'uk': 'Пошук',
               'ru': 'Поиск',
               'tr': 'Ara'
               },
    'formula': {'en': 'Formula',
                'uk': 'Формула',
                'ru': 'Формула',
                'tr': 'Formül'
               },
    'hint': {'en': 'Enter search query:',
             'uk': 'Введіть пошуковий запит:',
             'ru': 'Введите поисковой запрос:',
             'tr': 'Arama sorgusu girin'
            },
    'hint_desc': {'en': "(Do not delete bot's name 😮)",
                  'uk': "(Не видаляйте нікнейм бота 😮)",
                  'ru': "(Не удаляйте никнейм бота 😮)",
                  'tr': 'Bot takma adını silmeyin'
                 },
    'help_message': {'en': """This bot can work in your chats, you just need to add it there as a new member. Then call bot by typing its nickname: @WikipediaTelegraphBot in any chat with your query. This will open a panel with Wikipedia article hints. Tap on an item and bot will generate Telegraph page for you!

You can change language of articles anytime  by sending /set_language command to bot.""",
                     'uk': """Даний бот може працювати у Ваших чатах, Вам всього лише потрібно додати його в них як нового учасника. Далі викликаєте бота, вводячи його нік: @WikipediaTelegraphBot, ставите пробіл і запит з текстом, що Вас цікавить. Бот відповість на цей запит у вигляді випливаючих підказок з назвою вікі-статті. Якщо одна з підказок саме те, що Ви шукали, натискайте на неї і бот згенерує для Вас бажану Телеграф-сторінку, яку можна зручно переглянути у Instant View режимі!

Ви можете змінити мову статей у будь-який момент, надіславши боту команду /set_language.""",
                     'ru': """Этот бот может работать как и лично в Вашей переписке с ним, так и в Ваших чатах. Вам всего лишь нужно добавить его в них как нового участника. Далее вызываете бота, введя его ник:  @WikipediaTelegraphBot, ставите пробел и запрос с текстом, что вас интересует. Бот ответит на этот запрос в виде всплывающих подсказок с названием вики-статьи. Если одна из подсказок именно то, что Вы искали, нажимайте на неё и бот сгенерирует для Вас желаемую Телеграф-страницу, которую можно удобно просмотреть в Instant View режиме!

Вы можете изменить язык статей в любой момент, отправив боту комманду /set_language.""",
                    'tr': """Bu bot sohbetlerinizde çalışabilir. Bot yeni bir üye olarak sohbete eklemeniz yeterlidir. Sonra bot takma adını: @WikipediaTelegraphBot sorgunuz ile birlikte herhangi bir sohbete yazarak bot arayın. Vikipedi makale ipuçlarının yer aldığı bir panel açılacaktır. Bir öğeye dokunun ve bot sizin için Telegraph sayfasını oluşturacaktır!
Makalelerin dilini bota /set_language komutunu göndererek istediğiniz zaman değiştirebilirsiniz"""
                    },
    'rate': {'en': """If you like me, please give 5 stars ⭐️⭐️⭐️⭐️⭐️ rating at: https://telegram.me/storebot?start={}. Have a nice day!""".format(BOT_NAME, BOT_NAME),
             'uk': """Якщо я тобі подобаюсь, постав, будь ласка, 5 зірочок ⭐️⭐️⭐️⭐️⭐️ рейтингу на: https://telegram.me/storebot?start={}. Гарного дня!""".format(BOT_NAME, BOT_NAME),
             'ru': """Если я тебе понравился, поставь, пожалуйста, 5 звездочек ⭐️⭐️⭐️⭐️⭐️ рейтинга на: https://telegram.me/storebot?start={}. Хорошего дня!""".format(BOT_NAME, BOT_NAME),
             'tr': """If you like me, please give 5 stars ⭐️⭐️⭐️⭐️⭐️ rating at: https://telegram.me/storebot?start={}. Have a nice day!""".format(BOT_NAME, BOT_NAME)
             }
}

from bot import bot


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print(message)


def start_bot():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    start_bot()

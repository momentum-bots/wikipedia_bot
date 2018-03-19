from bot import bot
import wikipedia
import generate_telegraph


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = wikipedia.search(message.text)
    url = 'https://en.wikipedia.org/wiki/' + text[0].replace(' ', '_')
    print(url)
    response = generate_telegraph.generate_by_wiki_url(url)
    bot.send_message(message.chat.id, response)


def start_bot():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    start_bot()

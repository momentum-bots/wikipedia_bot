import flask
from telebot import types
from config import *
from bot_handlers import bot
from time import sleep

server = flask.Flask(__name__)


@server.route('/' + BOT_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, BOT_TOKEN))
    return "!", 200


if __name__ == '__main__':
    server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

import flask
from telebot import types
from config import *
from bot import bot
from time import sleep

app = flask.Flask(__name__)


@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


if __name__ == "__main__":
    bot.remove_webhook()
    sleep(1)
    bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                    certificate=open(WEBHOOK_SSL_CERT, 'r'))
    app.run(host=WEBHOOK_LISTEN,
            port=WEBHOOK_PORT,
            ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
            threaded=True
            )

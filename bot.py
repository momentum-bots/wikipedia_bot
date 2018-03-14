import config
import telebot

bot = telebot.TeleBot(config.bot_token)
print(bot.get_me())

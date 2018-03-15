import config
import telebot

bot = telebot.TeleBot(config.BOT_TOKEN)
print(bot.get_me())

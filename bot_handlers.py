from bot import bot
import wikipedia
import generate_telegraph
import re
from telebot import types
from time import sleep


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = wikipedia.search(message.text)
    try:
        url = 'https://en.wikipedia.org/wiki/' + text[0].replace(' ', '_')
        print(url)
        response = generate_telegraph.generate_by_wiki_url(url)
    except:
        response = 'Try again!'
    bot.send_message(message.chat.id, response)


@bot.inline_handler(func=lambda query: len(query.query) > 0)
def query_text(query):
    try:
        articles = []
        for article in wikipedia.search(query.query):
            if 'disambiguation' not in article:
                articles.append(article)
        buttons = []
        print(articles)
        for i, article in enumerate(articles):
            description = ''
            url = 'https://en.wikipedia.org/wiki/' + article.replace(' ', '_')
            buttons.append(types.InlineQueryResultArticle(
                           id=str(i), title=article,
                           description='test',
                           input_message_content=types.InputTextMessageContent(article)
            ))
        bot.answer_inline_query(query.id, buttons)
    except:
        print('fuck')
        return


    # print(query.query.split(' '))
    # num1, num2 = query.query.split(' ')
    #
    # try:
    #     m_sum = int(num1) + int(num2)
    #     r_sum = types.InlineQueryResultArticle(
    #             id='1', title="Сумма",
    #             # Описание отображается в подсказке,
    #             # message_text - то, что будет отправлено в виде сообщения
    #             description="Результат: {!s}".format(m_sum),
    #             input_message_content=types.InputTextMessageContent(
    #             message_text="{!s} + {!s} = {!s}".format(num1, num2, m_sum))
    #     )
    #     m_sub = int(num1) - int(num2)
    #     r_sub = types.InlineQueryResultArticle(
    #             id='2', title="Разность",
    #             description="Результат: {!s}".format(m_sub),
    #             input_message_content=types.InputTextMessageContent(
    #             message_text="{!s} - {!s} = {!s}".format(num1, num2, m_sub))
    #     )
    #     # Учтем деление на ноль и подготовим 2 варианта развития событий
    #     if num2 is not "0":
    #         m_div = int(num1) / int(num2)
    #         r_div = types.InlineQueryResultArticle(
    #                 id='3', title="Частное",
    #                 description="Результат: {0:.2f}".format(m_div),
    #                 input_message_content=types.InputTextMessageContent(
    #                 message_text="{0!s} / {1!s} = {2:.2f}".format(num1, num2, m_div))
    #         )
    #     else:
    #         r_div = types.InlineQueryResultArticle(
    #                 id='3', title="Частное", description="На ноль делить нельзя!",
    #                 input_message_content=types.InputTextMessageContent(
    #                 message_text="Я нехороший человек и делю на ноль!")
    #         )
    #     m_mul = int(num1) * int(num2)
    #     r_mul = types.InlineQueryResultArticle(
    #             id='4', title="Произведение",
    #             description="Результат: {!s}".format(m_mul),
    #             input_message_content=types.InputTextMessageContent(
    #             message_text="{!s} * {!s} = {!s}".format(num1, num2, m_mul))
    #     )
    #     bot.answer_inline_query(query.id, [r_sum, r_sub, r_div, r_mul])
    # except Exception as e:
    #     print("{!s}\n{!s}".format(type(e), str(e)))


def start_bot():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    start_bot()

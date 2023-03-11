from random import choice

from DecisionTeleBot.sqlite_db import add_new_data
from bot import bot
from messages import *
from config import ANSWERS


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, HELLO_MESSAGE)
    user_id = message.from_user.id
    user_lname = message.from_user.last_name
    user_fname = message.from_user.first_name
    username = message.from_user.username

    add_new_data(user_id=user_id, user_fname=user_fname, user_lname=user_lname, username=username)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, HELP_MESSAGE)


@bot.message_handler(content_types=["text"])
def get_response(message):
    if message.text[-1] == '?':
        bot.send_message(message.chat.id, choice(ANSWERS))
    else:
        bot.send_message(message.chat.id, 'Задай вопрос!')


if __name__ == '__main__':
    bot.polling(none_stop=True)

import telebot

from config import TOKEN

bot = telebot.TeleBot(TOKEN)
print(bot.get_me())

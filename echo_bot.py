import random
import telebot

TOKEN = ''
bot = telebot.TeleBot(TOKEN)

with open('film.txt', 'r', encoding="utf-8") as film:
 film = film.readlines() 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, random.choice(film))



@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
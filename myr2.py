import telebot
from telebot import types

bot = telebot.TeleBot('6768034981:AAGzZ2MjkrbO4SIlTXBagKi0MwoABoBlDrc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Здравствуйте')

@bot.message_handler(commands=['next'])
def start(message):
    bot.send_message(message.chat.id,'Что вы выбираете? Если хотите заказать нажмите на 1. Если вас интересует цена то нажмите на 2')
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='1', url="https://wa.me/700164046")
    btn2 = types.InlineKeyboardButton(text='2', url="https://www.instagram.com/lunai_style_1?igsh=Y3NiaGY0eTYyZDQy")
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, 'next', reply_markup=kb)

@bot.message_handler(commands=['bio'])
def start(message):
   bot.send_message(message.chat.id,'Ваши данные')
   kb=types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
   btn1=types.KeyboardButton(text='контакты',request_contact=True)
   btn2 = types.KeyboardButton(text='Местоположение', request_location=True)
   kb.add(btn1,btn2)
   bot.send_message(message.chat.id,'bio',reply_markup=kb)

bot.polling(none_stop=True)


























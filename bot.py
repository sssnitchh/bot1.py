import telebot
from telebot import types
import random

bot = telebot.TeleBot('6264262812:AAF7vcBudOv9BZs7l3xC7Fk23EpPCCXThhw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Играть")
    btn2 = types.KeyboardButton("Информация")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Информация"):
        bot.send_message(message.chat.id, text="Бот угадай число\nСделаный Владосом Русланом Евгением и Никитой")
    elif(message.text == "Играть"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(back)
        bot.send_message(message.chat.id, text="🎲", reply_markup=markup)
        bot.send_message(message.chat.id, text="Я загадал число, попробуй угадать", reply_markup=markup)
        bot.send_message(message.chat.id, text="Если угадаешь то я тебе сообщу", reply_markup=markup)
        bot.send_message(message.chat.id, text="Подсказка - оно двухзначное", reply_markup=markup)
        
    elif(message.text == random.randint(1,6)):

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        abutton1 = types.KeyboardButton("Играть")
        abutton2 = types.KeyboardButton("Информация")
        markup.add(abutton1, abutton2)
        bot.send_message(message.chat.id, "Верно! Возвращаю тебя в главное меню")
    
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Играть")
        button2 = types.KeyboardButton("Информация")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="С вовзращением!", reply_markup=markup)
  
bot.polling(none_stop=True, interval=0)
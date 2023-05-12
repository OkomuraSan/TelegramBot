import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
Token = "6118123405:AAEIUWlmgwva6m0G4NOHXeqZrO_L7lOcAoo"

def get_cat():
    response = requests.get("https://cataas.com/cat").content
    return response

def get_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random").json()
    return response["message"]


bot = telebot.TeleBot(Token)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Погода'))
keyboard.add(KeyboardButton('Об боте'))


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Я тестовый бот!', reply_markup=keyboard)

@bot.message_handler(func=lambda s: 'Погода' in s.text)
def get_weather_tel(message):
    weather = "Погода"
    bot.send_message(message.chat.id, weather)
@bot.message_handler(func=lambda s: "Об боте" in s.text)
def get_me(message):
    messages = "Это бот о погоде"
    bot.send_message(message.chat.id, messages)



bot.infinity_polling()


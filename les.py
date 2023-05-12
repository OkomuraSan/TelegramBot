import telebot
from telebot import types
Token = "6118123405:AAEIUWlmgwva6m0G4NOHXeqZrO_L7lOcAoo"
bot = telebot.TeleBot(Token)
last_message = None
About_bot = f"""
Я хороший бот и никого не обижу.
На данный момент я могу совсем мало всего, так что простите (┬┬﹏┬┬)
Но могу сделать две вещи (●'◡'●) :
    1) Решать примеры, наример, если вы напишите /calc 1+2 я отвечу 3, потому что я умный
    2) Я могу показытать погоду в месте, где ты живёшь, ( да я знаю, где ты живёшь (*/ω＼*) )
На этом всё. Спасибо за внимание"""
mode = None

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text="Функции") 
    btn2 = types.KeyboardButton(text="О боте")
    markup.add(btn1,btn2, row_width=3)
    bot.send_message(message.chat.id,"Привет", reply_markup=markup)
@bot.message_handler(commands=["calc"])
def calc(message):
    global last_message
    if message.text.split()[0] == "/calc":
        if len(message.text.split()) == 1:
            last_message = bot.send_message(message.chat.id, "/calc + пример")
        else:
            last_message = bot.send_message(message.chat.id, eval(str(message.text[6:])))



@bot.message_handler(content_types=['text'])
def functional_menu(message):
    global last_message
    global mode
    if message.text == "Функции":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton(text="Погода")
        btn_back = types.KeyboardButton(text="Назад")
        markup.add(btn4, btn_back, row_width=3)
        last_message = bot.send_message(message.chat.id, "Функции", reply_markup=markup)
        mode = None
    elif message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text="Функции")
        btn2 = types.KeyboardButton(text="О боте")
        markup.add(btn1, btn2, row_width=3)
        last_message = bot.send_message(message.chat.id, "Назад", reply_markup=markup)
        mode = None
    elif message.text == "О боте":
        last_message = bot.send_message(message.chat.id, About_bot)
    elif message.text == "Погода":
        last_message = bot.send_message(message.chat.id, "Ой... Это кнопка должна была показать погоду в месте, где вы живёте вплодь до второго пришествия, но... Я забыл это сделать, да и Марс сегодня в той фазе, когда я не вижу погоду... Простите")



    else:
        last_message = bot.send_message(message.chat.id, "Я не понимаю, что вы от меня хотите, я слишком глупый")

bot.polling()
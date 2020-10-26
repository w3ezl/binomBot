import telebot #добавляем в файл библиотеку pyTelegramBotAPI
from telebot import types #добавляем клавиатуру telegram
import config #добавляем в файл config.py
import str_data #добавляем в файл str_data.py

def kbd_main(): #создание функции
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for btn in str_data.btnsMain:
        keyboard.add(btn)
    return keyboard

bot = telebot.TeleBot(config.token, parse_mode="Markdown") #подключаем бота к телеграму

@bot.message_handler(commands=['start']) #реакция бота на команду start
def send_start(message): #создание функции
    bot.send_message(message.chat.id, str_data.startText, reply_markup=kbd_main()) #ответ бота

@bot.message_handler(content_types=['text']) #реакция бота на любое текстовое сообщение
def sent_text(message): #создание функции
    cAns = False
    for i in range(len(str_data.answMain)):
        if message.text == str_data.btnsMain[i]:
            bot.send_message(message.chat.id, str_data.answMain[i], reply_markup=kbd_main())
            cAns = True
    if cAns == False:
        bot.send_message(message.chat.id, str_data.textText, reply_markup=kbd_main()) #ответ бота

bot.polling() #закрытие бота
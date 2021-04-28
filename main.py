import telebot
from telebot import types
import sqlite3
from keyboa import keyboa_maker

token = ''
bot = telebot.TeleBot(token)

#Начальное меню
@bot.message_handler(commands=["start"])
def first(message):
    key = telebot.types.ReplyKeyboardMarkup(True,False)
    key.row("Получить расписание")
    key.row("Поиск аудитории")
    key.row("Справочник", "Помощь")
    send = bot.send_message(message.from_user.id, "Главное меню", reply_markup=key)
    bot.register_next_step_handler(send, second)

def second(message):
    if message.text == "Получить расписание":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("ФТТ", "ЮСТиП", "ФЭСиП")
        send = bot.send_message(message.from_user.id, "Выберите свой факультет:", reply_markup=keyboard)
        bot.register_next_step_handler(send,third)
    elif message.text == "Поиск аудитории":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("1 корпус", "2 корпус")
        send = bot.send_message(message.from_user.id, "Выберите корпус:", reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Пожалуйста, соблюдайте масочный режим')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECOwxgheCnp0hu1296--sN16O7LdrAyAACC8gBAAFji0YMVs1sFXX6JcgfBA')
        bot.register_next_step_handler(send, third)
    elif message.text == "Справочник":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Поиск преподователя")
        keyboard.row("Загрузка документов")
        send = bot.send_message(message.from_user.id, "Выберите нужный пункт", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)
    elif message.text == "Помощь":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Моя группа остуствует")
        keyboard.row("Связаться с администраицей")
        send = bot.send_message(message.from_user.id, "Выберите нужный пункт", reply_markup=keyboard)
        bot.register_next_step_handler(send, third)

def third(message):
    if message.text == "ФТТ":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("1 курс (ФТТ)")
        keyboard.row("2 курс (ФТТ)")
        keyboard.row("3 курс (ФТТ)")
        keyboard.row("4 курс (ФТТ)")
        send = bot.send_message(message.from_user.id, "3 уровень клавиатуры", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
    elif message.text == "ЮСТиП":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("1 курс (ЮСТиП)")
        keyboard.row("2 курс (ЮСТиП)")
        keyboard.row("3 курс (ЮСТиП)")
        keyboard.row("4 курс (ЮСТиП)")
        send = bot.send_message(message.from_user.id, "3 уровень клавиатуры", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
    elif message.text == "ФЭСиП":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("1 курс (ФЭСиП)")
        keyboard.row("2 курс (ФЭСиП)")
        keyboard.row("3 курс (ФЭСиП)")
        keyboard.row("4 курс (ФЭСиП)")
        send = bot.send_message(message.from_user.id, "3 уровень клавиатуры", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
    elif message.text == "1 корпус":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Кнопка 13", "Кнопка 14", "Назад на 2 уровень")
        send = bot.send_message(message.from_user.id, "3 уровень клавиатуры", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)
    elif message.text == "2 корпус":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("2248", "2241", "2243")
        send = bot.send_message(message.from_user.id, "Кабинеты 2 корпуса", reply_markup=keyboard)
        bot.register_next_step_handler(send, five)
    elif message.text == "Поиск преподователя":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("На главную")
        send = bot.send_message(message.from_user.id, "Пожалуйста, напишите фамилию преподователя:", reply_markup=keyboard)
        bot.register_next_step_handler(send, first)
    elif message.text == "Загрузка документов":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("Задолжности")
        send = bot.send_message(message.from_user.id, "Выберите нужный документ для загрузки:", reply_markup=keyboard)
        bot.register_next_step_handler(send, five)
    elif message.text == "Моя группа остуствует":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("На главную")
        send = bot.send_message(message.from_user.id, "Пожалуйста, попробуйте написать свою группу в чат. Если расписание не появлиось - напишите на эл.почту help@isoipbot.ru", reply_markup=keyboard)
        bot.register_next_step_handler(send, first)
    elif message.text == "Связаться с администраицей":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("На главную")
        send = bot.send_message(message.from_user.id, "Для связи с администрацией используйте эл.почту - help@isoipbot.ru \nСвзяаться с разработчиком @romitsu", reply_markup=keyboard)
        bot.register_next_step_handler(send, first)
#ИСТ-Тb11
def fourth(message):
    if message.text == "1 курс (ФТТ)":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("ИСТ-Тb11", "АПМ-Тb11", "БЖТ-Тb11")
        keyboard.row("ИКТС-Тb11", "ЭПА-Тb11", "ОБД-Тb11")
        send = bot.send_message(message.from_user.id, "3 уровень клавиатуры", reply_markup=keyboard)
        bot.register_next_step_handler(send, five)
    elif message.text == "ЮСТиП":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("1 курс (ЮСТиП)")
        keyboard.row("2 курс (ЮСТиП)")
        keyboard.row("3 курс (ЮСТиП)")
        keyboard.row("4 курс (ЮСТиП)")
        send = bot.send_message(message.from_user.id, "3 уровень клавиатуры", reply_markup=keyboard)
        bot.register_next_step_handler(send, fourth)

def five(message):
    if message.text == "ИСТ-Тb11":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("На главную")
        send = bot.send_message(message.from_user.id, "Расписание группы ИСТ-Тb41", reply_markup=keyboard)
        bot.send_message(message.chat.id, ist_tb11_str)
        bot.register_next_step_handler(send, first)
    elif message.text == "2248":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("На главную")
        send = bot.send_message(message.from_user.id, "Маршрут до 2248", reply_markup=keyboard)
        bot.send_message(message.chat.id, 'https://telegra.ph/Marshrut-2248-04-25')
        bot.register_next_step_handler(send, first)
    elif message.text == "Задолжности":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row("На главную")
        send = bot.send_message(message.from_user.id, "Приказ на отчисление", reply_markup=keyboard)
        file = open('19_04_2021.doc', 'rb')
        bot.send_document(message.chat.id, file)
        bot.register_next_step_handler(send, first)

#Работа с БД
base = sqlite3.connect('rasp1.db')
cur = base.cursor()
a = cur.execute('''SELECT * FROM ist''')
b = a.fetchall()
my_list = []
for x in b:
    my_list.append(' | '.join(x))
my_str = '\n'.join(my_list)
base.close()

base2 = sqlite3.connect('rasp_ist.db')
cur2 = base2.cursor()
a_ist_tb11 = cur2.execute('''SELECT * FROM ist_tb11''')
b_ist_tb11 = a_ist_tb11.fetchall()
ist_tb11_list = []
for x_ist_tb11 in b_ist_tb11:
    ist_tb11_list.append(' | '.join(x_ist_tb11))
ist_tb11_str = '\n'.join(ist_tb11_list)
base2.close()

img = "http://www.sssu.ru/portals/0/Kaf/isrt/2017/clip_image006.jpg"
tetx = "Береза А.Н. (доцент)"

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, my_str)
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока!')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECNwVggXmMsdcotss8NyZOlTWt2PwbVgACDcgBAAFji0YM5b2ONofFcO4fBA')
    elif message.text == 'береза':
        bot.send_message(message.chat.id, f'{tetx}\n{img}')

   # elif message.text.lower() == 'помощь':
    #    bot.send_message(message.chat.id, 'Если у вас что-то перестало работать, пожалуйста, перезапустите бота при помощи команды /start')
      #  bot.send_message(message.chat.id, 'Моей группы нет в разделе с расписанием! \nПопробуйте вручную написать название вашей группы. Если она отстуствует, напишите на help@isoipbot.ru')
    #elif message.text.lower() == 'ист':
     #   bot.send_message(message.chat.id, ist_tb11_str)

bot.polling()
import telebot
from telebot import types
import sqlite3
from datetime import datetime
from config import token

#ФТТ
from rasp import apa_tb11_str, apa_tb21_str, apa_tb31_str, apa_tb41_str, apm_tb11_str, apm_tb21_str, apm_tb31_str, apm_tb41_str
from rasp import bjt_tb11_str, bjt_tb21_str, bjt_tb31_str, bjt_tb41_str, ikts_tb11_str, ikts_tb21_str, ikts_tb31_str, ikts_tb41_str
from rasp import ist_tb11_str, ist_tb21_str, ist_tb31_str, ist_tb41_str, obd_tb11_str, obd_tb21_str, obd_tb31_str, obd_tb41_str
#ФЭСиП
from rasp import bu_ab11_str, bu_ab21_str, bu_ab31_str, turu_ab11_str, turu_ab21_str, turu_ab31_str
from rasp import up_ab11_str, up_ab21_str, up_ab31_str, up_ab41_str, au_ab11_str, au_ab21_str, au_ab31_str, au_ab41_str
#ЮСТиП
from rasp import grp_gb11_str, grp_gb21_str, grp_gb31_str, grp_gb41_str, grp_gbv11_str, grp_gbv21_str, grp_gbv31_str, grp_gbv41_str
from rasp import grp_gbvs11_str, grp_gbvs21_str, grp_gbvs31_str, grp_gbvs41_str, ugp_gb11_str, ugp_gb21_str, ugp_gb31_str, ugp_gb41_str

bot = telebot.TeleBot(token)

joinedFile = open('users.txt', 'r')
joinedUser = set()
for line in joinedFile:
    joinedUser.add(line.strip())
joinedFile.close()

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Получить расписание')
    keyboard.row('Поиск аудитории')
    keyboard.row('Справочник', 'Помощь')
    bot.send_message(message.chat.id, 'Скорее выбирай раздел в Главном меню – я знаю много интересного про институт!', reply_markup=keyboard)
    if not str(message.chat.id) in joinedUser:
        file = open('users.txt', 'a')
        file.write(str(message.chat.id) + '\n')
        file.close()

#spm

@bot.message_handler(content_types=["text"])
def any_msg(message):
    if message.text.lower() == 'получить расписание':
        keyrasp = types.InlineKeyboardMarkup(row_width=3)
        ftt_button = types.InlineKeyboardButton(text="ФТТ", callback_data="ftt")
        fasip_button = types.InlineKeyboardButton(text="ФЭСиП", callback_data="fasip")
        ustip_button = types.InlineKeyboardButton(text="ЮСТиП", callback_data="ustip")
        keyrasp.add(ftt_button, fasip_button, ustip_button)
        bot.send_message(message.chat.id, "Выберите свой факультет:", reply_markup=keyrasp)
    elif message.text.lower() == 'справочник':
        keyinfo = types.InlineKeyboardMarkup(row_width=1)
        teacher_button = types.InlineKeyboardButton(text="Поиск преподователя", callback_data="teacher")
        docs_button = types.InlineKeyboardButton(text="Загрузка документов", callback_data="docs")
        keyinfo.add(teacher_button, docs_button)
        bot.send_message(message.chat.id, "Выберите необходимый пункт:", reply_markup=keyinfo)
    elif message.text.lower() == 'поиск аудитории':
        bot.send_message(message.chat.id, 'Напишите номер необходимой аудитории в чат')
        bot.send_message(message.chat.id, 'Например: 2248')
        bot.send_message(message.chat.id, 'Пожалуйста, соблюдайте масочный режим')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECOwxgheCnp0hu1296--sN16O7LdrAyAACC8gBAAFji0YMVs1sFXX6JcgfBA')
    elif message.text.lower() == 'помощь':
        bot.send_message(message.chat.id, 'Для связи с администрацией используйте эл.почту - help@isoipbot.ru \nСвзяаться с разработчиком @romitsu')
    #Обработка поиска преподавателей
    elif message.text.lower() == 'береза':
        img_bereza = "http://www.sssu.ru/portals/0/Kaf/isrt/2017/clip_image006.jpg"
        text_bereza = "Береза Андрей Николаевич \nкандидат технических наук \nдоцент"
        bot.send_message(message.chat.id, f'{text_bereza}\n{img_bereza}')
        img_berezan = "http://www.sssu.ru/Portals/0/Kaf/isrt/11.jpg"
        text_berezan = "Береза Наталья Викторовна \nкандидат технических наук \nдоцент"
        bot.send_message(message.chat.id, f'{text_berezan}\n{img_berezan}')
    elif message.text.lower() == 'прокопенко':
        img_prokopenko = "http://www.sssu.ru/Portals/0/Kaf/isrt/prokopenko.jpg"
        text_prokopenko = "Прокопенко Николай  Николаевич \nзав. кафедрой \nдоктор технических наук \nпрофессор"
        bot.send_message(message.chat.id, f'{text_prokopenko}\n{img_prokopenko}')
    elif message.text.lower() == 'попов':
        img_popov = "http://www.sssu.ru/portals/0/Kaf/isrt/2017/clip_image004.jpg"
        text_popov = "Попов Алексей Эдуардович \nкандидат технических наук \nдоцент"
        bot.send_message(message.chat.id, f'{text_popov}\n{img_popov}')
    elif message.text.lower() == 'медведев':
        img_medvedev = "https://www.sssu.ru/Portals/0/2020/1/202006160.jpg"
        text_medvedev = "Медведев Дмитрий Викторович \nкандидат технических наук \nдоцент"
        bot.send_message(message.chat.id, f'{text_medvedev}\n{img_medvedev}')
    elif message.text.lower() == 'гавлицкий':
        img_gavlickiy = "http://www.sssu.ru/portals/0/Kaf/isrt/2017/clip_image012.jpg"
        text_gavlickiy = "Гавлицкий Александр Иванович \nкандидат технических наук \nдоцент"
        bot.send_message(message.chat.id, f'{text_gavlickiy}\n{img_gavlickiy}')
    elif message.text.lower() == 'ляшов':
        img_lyashov = "http://www.sssu.ru/Portals/0/Kaf/isrt/1111111.jpg"
        text_lyashov = "Ляшов Максим Васильевич \nкандидат технических наук \nдоцент"
        bot.send_message(message.chat.id, f'{text_lyashov}\n{img_lyashov}')
    elif message.text.lower() == 'бутырлагин':
        img_butyrlagin = "http://www.sssu.ru/portals/0/Kaf/isrt/2017/clip_image014.jpg"
        text_butyrlagin = "Бутырлагин Николай Владимирович \nкандидат технических наук \nдоцент"
        bot.send_message(message.chat.id, f'{text_butyrlagin}\n{img_butyrlagin}')
    elif message.text.lower() == 'лободенко':
        img_lobodenko = "http://www.sssu.ru/portals/0/Kaf/isrt/2017/clip_image016.jpg"
        text_lobodenko = "Лободенко Андрей Григорьевич \nстарший преподаватель"
        bot.send_message(message.chat.id, f'{text_lobodenko}\n{img_lobodenko}')
    elif message.text.lower() == 'балашова':
        img_balashova = "http://www.sssu.ru/portals/0/Kaf/isrt/2017/clip_image018.jpg"
        text_balashova = "Балашова Елена Владимировна \nстарший преподаватель"
        bot.send_message(message.chat.id, f'{text_balashova}\n{img_balashova}')
    elif message.text.lower() == 'морозов':
        img_morozov = "http://www.sssu.ru/portals/0/Kaf/isrt/2017/clip_image020.jpg"
        text_morozov = "Морозов Сергей Анатольевич \nстарший преподаватель"
        bot.send_message(message.chat.id, f'{text_morozov}\n{img_morozov}')
    elif message.text.lower() == 'бегляров':
        img_beglyarov = "http://www.sssu.ru/Portals/0/Kaf/isrt/13.jpg"
        text_beglyarov = "Бегляров Вадим Валерьевич \nкандидат технических наук \nдоцент"
        bot.send_message(message.chat.id, f'{text_beglyarov}\n{img_beglyarov}')
    elif message.text.lower() == 'коростылев':
        img_korostilev = "https://www.sssu.ru/Portals/0/2020/2021/1/%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8B%D0%BB%D0%B5%D0%B2.jpg"
        text_korostilev = "Коростылёв Максим Владимирович \nассистент"
        bot.send_message(message.chat.id, f'{text_korostilev}\n{img_korostilev}')
    elif message.text.lower() == 'шемякина':
        img_shemyakina = "https://www.sssu.ru/Portals/0/2020/2021/1/%D1%88%D0%B5%D0%BC%D1%8F%D0%BA%D0%B8%D0%BD%D0%B0.jpg"
        text_shemyakina = "Шемякина Марина Андреевна \nассистент"
        bot.send_message(message.chat.id, f'{text_shemyakina}\n{img_shemyakina}')
    elif message.text.lower() == 'заякина':
        img_zaykina = "http://www.sssu.ru/Portals/0/Kaf/isrt/1.png"
        text_zaykina = "Заякина Людмила Александровна \nинженер"
        bot.send_message(message.chat.id, f'{text_zaykina}\n{img_zaykina}')
    elif message.text.lower() == 'сергеева':
        img_sergeeva = "https://www.sssu.ru/Portals/0/2020/1/2020042701.jpg"
        text_sergeeva = "Сергеева Антонина Михайловна \nинженер"
        bot.send_message(message.chat.id, f'{text_sergeeva}\n{img_sergeeva}')
    # Обработка поиска аудиторий
    elif message.text.lower() == '2248':
        bot.send_message(message.chat.id, 'Аудитория 2248')
        bot.send_message(message.chat.id, 'https://telegra.ph/Marshrut-2248-04-25')

#keyboardmain
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "mainmenu":
        keyrasp = types.InlineKeyboardMarkup(row_width=3)
        ftt_button = types.InlineKeyboardButton(text="ФТТ", callback_data="ftt")
        fasip_button = types.InlineKeyboardButton(text="ФЭСиП", callback_data="fasip")
        ustip_button = types.InlineKeyboardButton(text="ЮСТиП", callback_data="ustip")
        keyrasp.add(ftt_button, fasip_button, ustip_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите свой факультет:",reply_markup=keyrasp)

    elif call.data == "maininfo":
        keyinfo = types.InlineKeyboardMarkup(row_width=1)
        teacher_button = types.InlineKeyboardButton(text="Поиск преподователя", callback_data="teacher")
        docs_button = types.InlineKeyboardButton(text="Загрузка документов", callback_data="docs")
        keyinfo.add(teacher_button, docs_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите необходимый пункт:",reply_markup=keyinfo)

    elif call.data == 'docs':
        keyboard_docs = types.InlineKeyboardMarkup(row_width=1)
        docs_but1 = types.InlineKeyboardButton(text="Заявка на выдачу справки-вызова ФТТ", callback_data="docs1")
        docs_but2 = types.InlineKeyboardButton(text="Заявка на выдачу справки-вызова ФЭСиП", callback_data="docs2")
        docs_but3 = types.InlineKeyboardButton(text="Заявка на выдачу справки-вызова ФЮСТиП", callback_data="docs3")
        docs_but4 = types.InlineKeyboardButton(text="Правила оформления письменных работ", callback_data="docs4")
        docs_but5 = types.InlineKeyboardButton(text="Правила применения шаблонов оформления", callback_data="docs5")
        docs_but6 = types.InlineKeyboardButton(text="Список задолжностей", callback_data="docs6")
        backbutton_info = types.InlineKeyboardButton(text="Назад", callback_data="maininfo")
        keyboard_docs.add(docs_but1, docs_but2, docs_but3, docs_but4, docs_but5, docs_but6, backbutton_info)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите нужный документ для загрузки:", reply_markup=keyboard_docs)

    elif call.data == "ftt":
        keyboard_ftt = types.InlineKeyboardMarkup(row_width=2)
        ftt_but_curs1 = types.InlineKeyboardButton(text="1 курс", callback_data="ftt_curs1")
        ftt_but_curs2 = types.InlineKeyboardButton(text="2 курс", callback_data="ftt_curs2")
        ftt_but_curs3 = types.InlineKeyboardButton(text="3 курс", callback_data="ftt_curs3")
        ftt_but_curs4 = types.InlineKeyboardButton(text="4 курс", callback_data="ftt_curs4")
        ftt_but_curs5 = types.InlineKeyboardButton(text="5 курс", callback_data="ftt_curs5")
        backbutton_ftt = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_ftt.add(ftt_but_curs1, ftt_but_curs2, ftt_but_curs3, ftt_but_curs4, ftt_but_curs5, backbutton_ftt)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите свой курс:",reply_markup=keyboard_ftt)

    elif call.data == "ftt_curs1":
        key_ftt_curs1 = types.InlineKeyboardMarkup(row_width=2)
        ftt_curs1_ist = types.InlineKeyboardButton(text="ИСТ-Тb11", callback_data="ist_tb11")
        ftt_curs1_apm = types.InlineKeyboardButton(text="АПМ-Тb11", callback_data="apm_tb11")
        ftt_curs1_bjt = types.InlineKeyboardButton(text="БЖТ-Тb11", callback_data="bjt_tb11")
        ftt_curs1_ikts = types.InlineKeyboardButton(text="ИКТС-Тb11", callback_data="ikts_tb11")
        ftt_curs1_apa = types.InlineKeyboardButton(text="ЭПА-Тb11", callback_data="apa_tb11")
        ftt_curs1_obd = types.InlineKeyboardButton(text="ОБД-Тb11", callback_data="obd_tb11")
        backbutton_ftt_curs1 = types.InlineKeyboardButton(text="Назад", callback_data="ftt")
        key_ftt_curs1.add(ftt_curs1_ist, ftt_curs1_apm, ftt_curs1_bjt, ftt_curs1_ikts, ftt_curs1_apa, ftt_curs1_obd, backbutton_ftt_curs1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_ftt_curs1)

    elif call.data == "ftt_curs2":
        key_ftt_curs2 = types.InlineKeyboardMarkup(row_width=2)
        ftt_curs2_ist = types.InlineKeyboardButton(text="ИСТ-Тb21", callback_data="ist_tb21")
        ftt_curs2_apm = types.InlineKeyboardButton(text="АПМ-Тb21", callback_data="apm_tb21")
        ftt_curs2_bjt = types.InlineKeyboardButton(text="БЖТ-Тb21", callback_data="bjt_tb21")
        ftt_curs2_ikts = types.InlineKeyboardButton(text="ИКТС-Тb21", callback_data="ikts_tb21")
        ftt_curs2_apa = types.InlineKeyboardButton(text="ЭПА-Тb21", callback_data="apa_tb21")
        ftt_curs2_obd = types.InlineKeyboardButton(text="ОБД-Тb21", callback_data="obd_tb21")
        backbutton_ftt_curs2 = types.InlineKeyboardButton(text="Назад", callback_data="ftt")
        key_ftt_curs2.add(ftt_curs2_ist, ftt_curs2_apm, ftt_curs2_bjt, ftt_curs2_ikts, ftt_curs2_apa, ftt_curs2_obd, backbutton_ftt_curs2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите свою группу:", reply_markup=key_ftt_curs2)

    elif call.data == "ftt_curs3":
        key_ftt_curs3 = types.InlineKeyboardMarkup(row_width=2)
        ftt_curs3_ist = types.InlineKeyboardButton(text="ИСТ-Тb31", callback_data="ist_tb31")
        ftt_curs3_apm = types.InlineKeyboardButton(text="АПМ-Тb31", callback_data="apm_tb31")
        ftt_curs3_bjt = types.InlineKeyboardButton(text="БЖТ-Тb31", callback_data="bjt_tb31")
        ftt_curs3_ikts = types.InlineKeyboardButton(text="ИКТС-Тb31", callback_data="ikts_tb31")
        ftt_curs3_apa = types.InlineKeyboardButton(text="ЭПА-Тb31", callback_data="apa_tb31")
        ftt_curs3_obd = types.InlineKeyboardButton(text="ОБД-Тb31", callback_data="obd_tb31")
        backbutton_ftt_curs3 = types.InlineKeyboardButton(text="Назад", callback_data="ftt")
        key_ftt_curs3.add(ftt_curs3_ist, ftt_curs3_apm, ftt_curs3_bjt, ftt_curs3_ikts, ftt_curs3_apa, ftt_curs3_obd, backbutton_ftt_curs3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите свою группу:", reply_markup=key_ftt_curs3)

    elif call.data == "ftt_curs4":
        key_ftt_curs4 = types.InlineKeyboardMarkup(row_width=2)
        ftt_curs4_ist = types.InlineKeyboardButton(text="ИСТ-Тb41", callback_data="ist_tb41")
        ftt_curs4_apm = types.InlineKeyboardButton(text="АПМ-Тb41", callback_data="apm_tb41")
        ftt_curs4_bjt = types.InlineKeyboardButton(text="БЖТ-Тb41", callback_data="bjt_tb41")
        ftt_curs4_ikts = types.InlineKeyboardButton(text="ИКТС-Тb41", callback_data="ikts_tb41")
        ftt_curs4_apa = types.InlineKeyboardButton(text="ЭПА-Тb41", callback_data="apa_tb41")
        ftt_curs4_obd = types.InlineKeyboardButton(text="ОБД-Тb41", callback_data="obd_tb41")
        backbutton_ftt_curs4 = types.InlineKeyboardButton(text="Назад", callback_data="ftt")
        key_ftt_curs4.add(ftt_curs4_ist, ftt_curs4_apm, ftt_curs4_bjt, ftt_curs4_ikts, ftt_curs4_apa, ftt_curs4_obd, backbutton_ftt_curs4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Выберите свою группу:", reply_markup=key_ftt_curs4)
#Конец блока с ФТТ
    elif call.data == "fasip":
        keyboard_fasip = types.InlineKeyboardMarkup(row_width=2)
        fasip_but_curs1 = types.InlineKeyboardButton(text="1 курс", callback_data="fasip_curs1")
        fasip_but_curs2 = types.InlineKeyboardButton(text="2 курс", callback_data="fasip_curs2")
        fasip_but_curs3 = types.InlineKeyboardButton(text="3 курс", callback_data="fasip_curs3")
        fasip_but_curs4 = types.InlineKeyboardButton(text="4 курс", callback_data="fasip_curs4")
        fasip_but_curs5 = types.InlineKeyboardButton(text="5 курс", callback_data="fasip_curs5")
        backbutton_fasip = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_fasip.add(fasip_but_curs1, fasip_but_curs2, fasip_but_curs3, fasip_but_curs4, fasip_but_curs5, backbutton_fasip)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите свой курс:",reply_markup=keyboard_fasip)

    elif call.data == "fasip_curs1":
        key_fasip_curs1 = types.InlineKeyboardMarkup(row_width=2)
        fasip_curs1_bu = types.InlineKeyboardButton(text="БУ-Эb11", callback_data="bu_ab11")
        fasip_curs1_turu = types.InlineKeyboardButton(text="ТУРУ-Эb11", callback_data="turu_ab11")
        fasip_curs1_up = types.InlineKeyboardButton(text="УП-Эb11", callback_data="up_ab11")
        fasip_curs1_au = types.InlineKeyboardButton(text="ЭУ-Эb11", callback_data="au_ab11")
        backbutton_fasip_curs1 = types.InlineKeyboardButton(text="Назад", callback_data="fasip")
        key_fasip_curs1.add(fasip_curs1_bu, fasip_curs1_turu, fasip_curs1_up, fasip_curs1_au, backbutton_fasip_curs1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_fasip_curs1)

    elif call.data == "fasip_curs2":
        key_fasip_curs2 = types.InlineKeyboardMarkup(row_width=2)
        fasip_curs2_bu = types.InlineKeyboardButton(text="БУ-Эb21", callback_data="bu_ab21")
        fasip_curs2_turu = types.InlineKeyboardButton(text="ТУРУ-Эb21", callback_data="turu_ab21")
        fasip_curs2_up = types.InlineKeyboardButton(text="УП-Эb21", callback_data="up_ab21")
        fasip_curs2_au = types.InlineKeyboardButton(text="ЭУ-Эb21", callback_data="au_ab21")
        backbutton_fasip_curs2 = types.InlineKeyboardButton(text="Назад", callback_data="fasip")
        key_fasip_curs2.add(fasip_curs2_bu, fasip_curs2_turu, fasip_curs2_up, fasip_curs2_au, backbutton_fasip_curs2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_fasip_curs2)

    elif call.data == "fasip_curs3":
        key_fasip_curs3 = types.InlineKeyboardMarkup(row_width=2)
        fasip_curs3_bu = types.InlineKeyboardButton(text="БУ-Эb31", callback_data="bu_ab31")
        fasip_curs3_turu = types.InlineKeyboardButton(text="ТУРУ-Эb31", callback_data="turu_ab31")
        fasip_curs3_up = types.InlineKeyboardButton(text="УП-Эb31", callback_data="up_ab31")
        fasip_curs3_au = types.InlineKeyboardButton(text="ЭУ-Эb31", callback_data="au_ab31")
        backbutton_fasip_curs3 = types.InlineKeyboardButton(text="Назад", callback_data="fasip")
        key_fasip_curs3.add(fasip_curs3_bu, fasip_curs3_turu, fasip_curs3_up, fasip_curs3_au, backbutton_fasip_curs3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_fasip_curs3)

    elif call.data == "fasip_curs4":
        key_fasip_curs4 = types.InlineKeyboardMarkup(row_width=2)
        fasip_curs4_up = types.InlineKeyboardButton(text="УП-Эb41", callback_data="up_ab41")
        fasip_curs4_au = types.InlineKeyboardButton(text="ЭУ-Эb41", callback_data="au_ab41")
        backbutton_fasip_curs4 = types.InlineKeyboardButton(text="Назад", callback_data="fasip")
        key_fasip_curs4.add(fasip_curs4_up, fasip_curs4_au, backbutton_fasip_curs4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_fasip_curs4)

    elif call.data == "ustip":
        keyboard_ustip = types.InlineKeyboardMarkup(row_width=2)
        ustip_but_curs1 = types.InlineKeyboardButton(text="1 курс", callback_data="ustip_curs1")
        ustip_but_curs2 = types.InlineKeyboardButton(text="2 курс", callback_data="ustip_curs2")
        ustip_but_curs3 = types.InlineKeyboardButton(text="3 курс", callback_data="ustip_curs3")
        ustip_but_curs4 = types.InlineKeyboardButton(text="4 курс", callback_data="ustip_curs4")
        ustip_but_curs5 = types.InlineKeyboardButton(text="5 курс", callback_data="ustip_curs5")
        backbutton_ustip = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_ustip.add(ustip_but_curs1, ustip_but_curs2, ustip_but_curs3, ustip_but_curs4, ustip_but_curs5, backbutton_ustip)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите свой курс:",reply_markup=keyboard_ustip)

    elif call.data == "ustip_curs1":
        key_ustip_curs1 = types.InlineKeyboardMarkup(row_width=2)
        ustip_curs1_bu = types.InlineKeyboardButton(text="ГРП-Гb11", callback_data="grp_gb11")
        ustip_curs1_turu = types.InlineKeyboardButton(text="ГРП-Гbv11", callback_data="grp_gbv11")
        ustip_curs1_up = types.InlineKeyboardButton(text="ГРП-Гbvs11", callback_data="grp_gbvs11")
        ustip_curs1_au = types.InlineKeyboardButton(text="УГП-Гb11", callback_data="ugp_gb11")
        backbutton_ustip_curs1 = types.InlineKeyboardButton(text="Назад", callback_data="ustip")
        key_ustip_curs1.add(ustip_curs1_bu, ustip_curs1_turu, ustip_curs1_up, ustip_curs1_au, backbutton_ustip_curs1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_ustip_curs1)

    elif call.data == "ustip_curs2":
        key_ustip_curs2 = types.InlineKeyboardMarkup(row_width=2)
        ustip_curs2_bu = types.InlineKeyboardButton(text="ГРП-Гb21", callback_data="grp_gb21")
        ustip_curs2_turu = types.InlineKeyboardButton(text="ГРП-Гbv21", callback_data="grp_gbv21")
        ustip_curs2_up = types.InlineKeyboardButton(text="ГРП-Гbvs21", callback_data="ugp_gb21")
        ustip_curs2_au = types.InlineKeyboardButton(text="УГП-Гb21", callback_data="ugp_gb21")
        backbutton_ustip_curs2 = types.InlineKeyboardButton(text="Назад", callback_data="ustip")
        key_ustip_curs2.add(ustip_curs2_bu, ustip_curs2_turu, ustip_curs2_up, ustip_curs2_au, backbutton_ustip_curs2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_ustip_curs2)

    elif call.data == "ustip_curs3":
        key_ustip_curs3 = types.InlineKeyboardMarkup(row_width=2)
        ustip_curs3_bu = types.InlineKeyboardButton(text="ГРП-Гb31", callback_data="grp_gb31")
        ustip_curs3_turu = types.InlineKeyboardButton(text="ГРП-Гbv31", callback_data="grp_gbv31")
        ustip_curs3_up = types.InlineKeyboardButton(text="ГРП-Гbvs31", callback_data="ugp_gb31")
        ustip_curs3_au = types.InlineKeyboardButton(text="УГП-Гb31", callback_data="ugp_gb31")
        backbutton_ustip_curs3 = types.InlineKeyboardButton(text="Назад", callback_data="ustip")
        key_ustip_curs3.add(ustip_curs3_bu, ustip_curs3_turu, ustip_curs3_up, ustip_curs3_au, backbutton_ustip_curs3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_ustip_curs3)

    elif call.data == "ustip_curs4":
        key_ustip_curs4 = types.InlineKeyboardMarkup(row_width=2)
        ustip_curs4_bu = types.InlineKeyboardButton(text="ГРП-Гb41", callback_data="grp_gb41")
        ustip_curs4_turu = types.InlineKeyboardButton(text="ГРП-Гbv41", callback_data="grp_gbv41")
        ustip_curs4_up = types.InlineKeyboardButton(text="ГРП-Гbvs41", callback_data="ugp_gb41")
        ustip_curs4_au = types.InlineKeyboardButton(text="УГП-Гb41", callback_data="ugp_gb41")
        backbutton_ustip_curs4 = types.InlineKeyboardButton(text="Назад", callback_data="ustip")
        key_ustip_curs4.add(ustip_curs4_up, ustip_curs4_au, backbutton_ustip_curs4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_ustip_curs4)
# Конец блока с ФЭСиП
    elif call.data == 'teacher':
        bot.send_message(call.message.chat.id, 'Пожалуйста, напишите фамилию преподавателя')
        bot.send_message(call.message.chat.id, 'Например: Попов')

    elif call.data == 'fasip_curs5':
        bot.send_message(call.message.chat.id, 'Извините, групп не найдено')

    elif call.data == 'ftt_curs5':
        bot.send_message(call.message.chat.id, 'Извините, групп не найдено')

    elif call.data == 'ustip_curs5':
        bot.send_message(call.message.chat.id, 'Извините, групп не найдено')

    #Факультет ФТТ
    elif call.data == 'apa_tb11':
        bot.send_message(call.message.chat.id, 'Расписание ЭПА-Тb11')
        bot.send_message(call.message.chat.id, apa_tb11_str)

    elif call.data == 'apa_tb21':
        bot.send_message(call.message.chat.id, 'Расписание ЭПА-Тb21')
        bot.send_message(call.message.chat.id, apa_tb21_str)

    elif call.data == 'apa_tb31':
        bot.send_message(call.message.chat.id, 'Расписание ЭПА-Тb31')
        bot.send_message(call.message.chat.id, apa_tb31_str)

    elif call.data == 'apa_tb41':
        bot.send_message(call.message.chat.id, 'Расписание ЭПА-Тb41')
        bot.send_message(call.message.chat.id, apa_tb41_str)

    elif call.data == 'apm_tb11':
        bot.send_message(call.message.chat.id, 'Расписание АПМ-Тb11')
        bot.send_message(call.message.chat.id, apm_tb11_str)

    elif call.data == 'apm_tb21':
        bot.send_message(call.message.chat.id, 'Расписание АПМ-Тb21')
        bot.send_message(call.message.chat.id, apm_tb21_str)

    elif call.data == 'apm_tb31':
        bot.send_message(call.message.chat.id, 'Расписание АПМ-Тb31')
        bot.send_message(call.message.chat.id, apm_tb31_str)

    elif call.data == 'apm_tb41':
        bot.send_message(call.message.chat.id, 'Расписание АПМ-Тb41')
        bot.send_message(call.message.chat.id, apm_tb41_str)

    elif call.data == 'bjt_tb11':
        bot.send_message(call.message.chat.id, 'Расписание БЖТ-Тb11')
        bot.send_message(call.message.chat.id, bjt_tb11_str)

    elif call.data == 'bjt_tb21':
        bot.send_message(call.message.chat.id, 'Расписание БЖТ-Тb21')
        bot.send_message(call.message.chat.id, bjt_tb21_str)

    elif call.data == 'bjt_tb31':
        bot.send_message(call.message.chat.id, 'Расписание БЖТ-Тb31')
        bot.send_message(call.message.chat.id, bjt_tb31_str)

    elif call.data == 'bjt_tb41':
        bot.send_message(call.message.chat.id, 'Расписание БЖТ-Тb41')
        bot.send_message(call.message.chat.id, bjt_tb41_str)

    elif call.data == 'ikts_tb11':
        bot.send_message(call.message.chat.id, 'Расписание ИКТС-Тb11')
        bot.send_message(call.message.chat.id, ikts_tb11_str)

    elif call.data == 'ikts_tb21':
        bot.send_message(call.message.chat.id, 'Расписание ИКТС-Тb21')
        bot.send_message(call.message.chat.id, ikts_tb21_str)

    elif call.data == 'ikts_tb31':
        bot.send_message(call.message.chat.id, 'Расписание ИКТС-Тb31')
        bot.send_message(call.message.chat.id, ikts_tb31_str)

    elif call.data == 'ikts_tb41':
        bot.send_message(call.message.chat.id, 'Расписание ИКТС-Тb41')
        bot.send_message(call.message.chat.id, ikts_tb41_str)

    elif call.data == 'ist_tb11':
        bot.send_message(call.message.chat.id, 'Расписание ИСТ-Тb11')
        bot.send_message(call.message.chat.id, ist_tb11_str)

    elif call.data == 'ist_tb21':
        bot.send_message(call.message.chat.id, 'Расписание ИСТ-Тb21')
        bot.send_message(call.message.chat.id, ist_tb21_str)

    elif call.data == 'ist_tb31':
        bot.send_message(call.message.chat.id, 'Расписание ИСТ-Тb31')
        bot.send_message(call.message.chat.id, ist_tb31_str)

    elif call.data == 'ist_tb41':
        bot.send_message(call.message.chat.id, 'Расписание ИСТ-Тb41')
        bot.send_message(call.message.chat.id, ist_tb41_str)

    elif call.data == 'obd_tb11':
        bot.send_message(call.message.chat.id, 'Расписание ОБД-Тb11')
        bot.send_message(call.message.chat.id, obd_tb11_str)

    elif call.data == 'obd_tb21':
        bot.send_message(call.message.chat.id, 'Расписание ОБД-Тb21')
        bot.send_message(call.message.chat.id, obd_tb21_str)

    elif call.data == 'obd_tb31':
        bot.send_message(call.message.chat.id, 'Расписание ОБД-Тb31')
        bot.send_message(call.message.chat.id, obd_tb31_str)

    elif call.data == 'obd_tb41':
        bot.send_message(call.message.chat.id, 'Расписание ОБД-Тb41')
        bot.send_message(call.message.chat.id, obd_tb41_str)
    # Факультет ФЭСиП
    elif call.data == 'bu_ab11':
        bot.send_message(call.message.chat.id, 'Расписание БУ-Эb11')
        bot.send_message(call.message.chat.id, bu_ab11_str)

    elif call.data == 'bu_ab21':
        bot.send_message(call.message.chat.id, 'Расписание БУ-Эb21')
        bot.send_message(call.message.chat.id, bu_ab21_str)

    elif call.data == 'bu_ab31':
        bot.send_message(call.message.chat.id, 'Расписание БУ-Эb31')
        bot.send_message(call.message.chat.id, bu_ab31_str)

    elif call.data == 'turu_ab11':
        bot.send_message(call.message.chat.id, 'Расписание ТУРУ-Эb11')
        bot.send_message(call.message.chat.id, turu_ab11_str)

    elif call.data == 'turu_ab21':
        bot.send_message(call.message.chat.id, 'Расписание ТУРУ-Эb21')
        bot.send_message(call.message.chat.id, turu_ab21_str)

    elif call.data == 'turu_ab31':
        bot.send_message(call.message.chat.id, 'Расписание ТУРУ-Эb31')
        bot.send_message(call.message.chat.id, turu_ab31_str)

    elif call.data == 'up_ab11':
        bot.send_message(call.message.chat.id, 'Расписание УП-Эb11')
        bot.send_message(call.message.chat.id, up_ab11_str)

    elif call.data == 'up_ab21':
        bot.send_message(call.message.chat.id, 'Расписание УП-Эb21')
        bot.send_message(call.message.chat.id, up_ab21_str)

    elif call.data == 'up_ab31':
        bot.send_message(call.message.chat.id, 'Расписание УП-Эb31')
        bot.send_message(call.message.chat.id, up_ab31_str)

    elif call.data == 'up_ab41':
        bot.send_message(call.message.chat.id, 'Расписание УП-Эb41')
        bot.send_message(call.message.chat.id, up_ab41_str)

    elif call.data == 'au_ab11':
        bot.send_message(call.message.chat.id, 'Расписание ЭУ-Эb11')
        bot.send_message(call.message.chat.id, au_ab11_str)

    elif call.data == 'au_ab21':
        bot.send_message(call.message.chat.id, 'Расписание ЭУ-Эb21')
        bot.send_message(call.message.chat.id, au_ab21_str)

    elif call.data == 'au_ab31':
        bot.send_message(call.message.chat.id, 'Расписание ЭУ-Эb31')
        bot.send_message(call.message.chat.id, au_ab31_str)

    elif call.data == 'au_ab41':
        bot.send_message(call.message.chat.id, 'Расписание ЭУ-Эb41')
        bot.send_message(call.message.chat.id, au_ab41_str)
    #ЮСТиП
    elif call.data == 'grp_gb11':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гb11')
        bot.send_message(call.message.chat.id, grp_gb11_str)

    elif call.data == 'grp_gb21':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гb21')
        bot.send_message(call.message.chat.id, grp_gb21_str)

    elif call.data == 'grp_gb31':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гb31')
        bot.send_message(call.message.chat.id, grp_gb31_str)

    elif call.data == 'grp_gb41':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гb41')
        bot.send_message(call.message.chat.id, grp_gb41_str)

    elif call.data == 'grp_gbv11':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbv11')
        bot.send_message(call.message.chat.id, grp_gbv11_str)

    elif call.data == 'grp_gbv21':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbv21')
        bot.send_message(call.message.chat.id, grp_gbv21_str)

    elif call.data == 'grp_gbv31':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbv31')
        bot.send_message(call.message.chat.id, grp_gbv31_str)

    elif call.data == 'grp_gbv41':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbv41')
        bot.send_message(call.message.chat.id, grp_gbv41_str)

    elif call.data == 'grp_gbvs11':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbvs11')
        bot.send_message(call.message.chat.id, grp_gbvs11_str)

    elif call.data == 'grp_gbvs21':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbvs21')
        bot.send_message(call.message.chat.id, grp_gbvs21_str)

    elif call.data == 'grp_gbvs31':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbvs31')
        bot.send_message(call.message.chat.id, grp_gbvs31_str)

    elif call.data == 'grp_gbvs41':
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbvs41')
        bot.send_message(call.message.chat.id, grp_gbvs41_str)

    elif call.data == 'ugp_gb11':
        bot.send_message(call.message.chat.id, 'Расписание УГП-Гb11')
        bot.send_message(call.message.chat.id, ugp_gb11_str)

    elif call.data == 'ugp_gb21':
        bot.send_message(call.message.chat.id, 'Расписание УГП-Гb21')
        bot.send_message(call.message.chat.id, ugp_gb21_str)

    elif call.data == 'ugp_gb31':
        bot.send_message(call.message.chat.id, 'Расписание УГП-Гb31')
        bot.send_message(call.message.chat.id, ugp_gb31_str)

    elif call.data == 'ugp_gb41':
        bot.send_message(call.message.chat.id, 'Расписание УГП-Гb41')
        bot.send_message(call.message.chat.id, ugp_gb41_str)
    #Документы:
    elif call.data == 'docs1':
        bot.send_message(call.message.chat.id, 'Заявка на выдачу справки-вызова ФТТ')
        file1 = open('docs/ftt.docx', 'rb')
        bot.send_document(call.message.chat.id, file1)

    elif call.data == 'docs2':
        bot.send_message(call.message.chat.id, 'Заявка на выдачу справки-вызова ФЭСиП')
        file2 = open('docs/fasip.doc', 'rb')
        bot.send_document(call.message.chat.id, file2)

    elif call.data == 'docs3':
        bot.send_message(call.message.chat.id, 'Заявка на выдачу справки-вызова ФЮСТиП')
        file3 = open('docs/ustip.doc', 'rb')
        bot.send_document(call.message.chat.id, file3)

    elif call.data == 'docs4':
        bot.send_message(call.message.chat.id, 'Правила оформления письменных работ')
        file4 = open('docs/242pr.pdf', 'rb')
        bot.send_document(call.message.chat.id, file4)

    elif call.data == 'docs5':
        bot.send_message(call.message.chat.id, 'Правила применения шаблонов оформления')
        file5 = open('docs/242sh.pdf', 'rb')
        bot.send_document(call.message.chat.id, file5)

    elif call.data == 'docs6':
        bot.send_message(call.message.chat.id, 'Список задолжностей')
        file6 = open('docs/dolg.doc', 'rb')
        bot.send_document(call.message.chat.id, file6)

    return call

current_datetime = datetime.now()
print("Бот запущен:")
print(current_datetime)

bot.polling(none_stop=True, interval=0)

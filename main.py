import telebot
from telebot import types
import sqlite3
from config import token

from rasp import ist_tb11_str, ist_tb21_str, ist_tb31_str, ist_tb41_str

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Получить расписание')
    keyboard.row('Поиск аудитории')
    keyboard.row('Справочник', 'Помощь')
    bot.send_message(message.chat.id, 'Добро пожаловать в стартовое меню!', reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def any_msg(message):
    if message.text.lower() == 'получить расписание':
        keyrasp = types.InlineKeyboardMarkup(row_width=3)
        ftt_button = types.InlineKeyboardButton(text="ФТТ", callback_data="ftt")
        fasip_button = types.InlineKeyboardButton(text="ФЭСиП", callback_data="fasip")
        ustip_button = types.InlineKeyboardButton(text="ЮСТиП", callback_data="ustip")
        keyrasp.add(ftt_button, fasip_button, ustip_button)
        bot.send_message(message.chat.id, "Выберите свой факультет:", reply_markup=keyrasp)

    elif message.text.lower() == 'береза':
        img = "http://www.sssu.ru/portals/0/Kaf/isrt/2017/clip_image006.jpg"
        tetx = "Береза А.Н. (доцент)"
        bot.send_message(message.chat.id, f'{tetx}\n{img}')
    elif message.text.lower() == 'поиск аудитории':
        bot.send_message(message.chat.id, 'Напишите номер необходимой аудитории в чат')
        bot.send_message(message.chat.id, 'Например: 2248')
        bot.send_message(message.chat.id, 'Пожалуйста, соблюдайте масочный режим')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECOwxgheCnp0hu1296--sN16O7LdrAyAACC8gBAAFji0YMVs1sFXX6JcgfBA')
    elif message.text.lower() == 'помощь':
        bot.send_message(message.chat.id, 'Для связи с администрацией используйте эл.почту - help@isoipbot.ru \nСвзяаться с разработчиком @romitsu')


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

    if call.data == "ftt":
        keyboard_ftt = types.InlineKeyboardMarkup(row_width=2)
        ftt_but_curs1 = types.InlineKeyboardButton(text="1 курс", callback_data="ftt_curs1")
        ftt_but_curs2 = types.InlineKeyboardButton(text="2 курс", callback_data="ftt_curs2")
        ftt_but_curs3 = types.InlineKeyboardButton(text="3 курс", callback_data="ftt_curs3")
        ftt_but_curs4 = types.InlineKeyboardButton(text="4 курс", callback_data="ftt_curs4")
        ftt_but_curs5 = types.InlineKeyboardButton(text="5 курс", callback_data="ftt_curs5")
        backbutton_ftt = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_ftt.add(ftt_but_curs1, ftt_but_curs2, ftt_but_curs3, ftt_but_curs4, ftt_but_curs5, backbutton_ftt)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите свой курс:",reply_markup=keyboard_ftt)

    if call.data == "ftt_curs1":
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

    if call.data == "ftt_curs2":
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

    if call.data == "ftt_curs3":
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

    if call.data == "ftt_curs4":
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
    if call.data == "fasip":
        keyboard_fasip = types.InlineKeyboardMarkup(row_width=2)
        fasip_but_curs1 = types.InlineKeyboardButton(text="1 курс", callback_data="fasip_curs1")
        fasip_but_curs2 = types.InlineKeyboardButton(text="2 курс", callback_data="fasip_curs2")
        fasip_but_curs3 = types.InlineKeyboardButton(text="3 курс", callback_data="fasip_curs3")
        fasip_but_curs4 = types.InlineKeyboardButton(text="4 курс", callback_data="fasip_curs4")
        fasip_but_curs5 = types.InlineKeyboardButton(text="5 курс", callback_data="fasip_curs5")
        backbutton_fasip = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_fasip.add(fasip_but_curs1, fasip_but_curs2, fasip_but_curs3, fasip_but_curs4, fasip_but_curs5, backbutton_fasip)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите свой курс:",reply_markup=keyboard_fasip)

    if call.data == "fasip_curs1":
        key_fasip_curs1 = types.InlineKeyboardMarkup(row_width=2)
        fasip_curs1_bu = types.InlineKeyboardButton(text="БУ-Эb11", callback_data="bu_ab11")
        fasip_curs1_turu = types.InlineKeyboardButton(text="ТУРУ-Эb11", callback_data="turu_ab11")
        fasip_curs1_up = types.InlineKeyboardButton(text="УП-Эb11", callback_data="up_ab11")
        fasip_curs1_au = types.InlineKeyboardButton(text="ЭУ-Эb11", callback_data="au_ab11")
        backbutton_fasip_curs1 = types.InlineKeyboardButton(text="Назад", callback_data="fasip")
        key_fasip_curs1.add(fasip_curs1_bu, fasip_curs1_turu, fasip_curs1_up, fasip_curs1_au, backbutton_fasip_curs1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_fasip_curs1)

    if call.data == "fasip_curs2":
        key_fasip_curs2 = types.InlineKeyboardMarkup(row_width=2)
        fasip_curs2_bu = types.InlineKeyboardButton(text="БУ-Эb21", callback_data="bu_ab21")
        fasip_curs2_turu = types.InlineKeyboardButton(text="ТУРУ-Эb21", callback_data="turu_ab21")
        fasip_curs2_up = types.InlineKeyboardButton(text="УП-Эb21", callback_data="up_ab21")
        fasip_curs2_au = types.InlineKeyboardButton(text="ЭУ-Эb21", callback_data="au_ab21")
        backbutton_fasip_curs2 = types.InlineKeyboardButton(text="Назад", callback_data="fasip")
        key_fasip_curs2.add(fasip_curs2_bu, fasip_curs2_turu, fasip_curs2_up, fasip_curs2_au, backbutton_fasip_curs2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_fasip_curs2)

    if call.data == "fasip_curs3":
        key_fasip_curs3 = types.InlineKeyboardMarkup(row_width=2)
        fasip_curs3_bu = types.InlineKeyboardButton(text="БУ-Эb31", callback_data="bu_ab31")
        fasip_curs3_turu = types.InlineKeyboardButton(text="ТУРУ-Эb31", callback_data="turu_ab31")
        fasip_curs3_up = types.InlineKeyboardButton(text="УП-Эb31", callback_data="up_ab31")
        fasip_curs3_au = types.InlineKeyboardButton(text="ЭУ-Эb31", callback_data="au_ab31")
        backbutton_fasip_curs3 = types.InlineKeyboardButton(text="Назад", callback_data="fasip")
        key_fasip_curs3.add(fasip_curs3_bu, fasip_curs3_turu, fasip_curs3_up, fasip_curs3_au, backbutton_fasip_curs3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_fasip_curs3)

    if call.data == "fasip_curs4":
        key_fasip_curs4 = types.InlineKeyboardMarkup(row_width=2)
        fasip_curs4_up = types.InlineKeyboardButton(text="УП-Эb41", callback_data="up_ab41")
        fasip_curs4_au = types.InlineKeyboardButton(text="ЭУ-Эb41", callback_data="au_ab41")
        backbutton_fasip_curs4 = types.InlineKeyboardButton(text="Назад", callback_data="fasip")
        key_fasip_curs4.add(fasip_curs4_up, fasip_curs4_au, backbutton_fasip_curs4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_fasip_curs4)


    if call.data == "ustip":
        keyboard_ustip = types.InlineKeyboardMarkup(row_width=2)
        ustip_but_curs1 = types.InlineKeyboardButton(text="1 курс", callback_data="ustip_curs1")
        ustip_but_curs2 = types.InlineKeyboardButton(text="2 курс", callback_data="ustip_curs2")
        ustip_but_curs3 = types.InlineKeyboardButton(text="3 курс", callback_data="ustip_curs3")
        ustip_but_curs4 = types.InlineKeyboardButton(text="4 курс", callback_data="ustip_curs4")
        ustip_but_curs5 = types.InlineKeyboardButton(text="5 курс", callback_data="ustip_curs5")
        backbutton_ustip = types.InlineKeyboardButton(text="Назад", callback_data="mainmenu")
        keyboard_ustip.add(ustip_but_curs1, ustip_but_curs2, ustip_but_curs3, ustip_but_curs4, ustip_but_curs5, backbutton_ustip)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите свой курс:",reply_markup=keyboard_ustip)

    if call.data == "ustip_curs1":
        key_ustip_curs1 = types.InlineKeyboardMarkup(row_width=2)
        ustip_curs1_bu = types.InlineKeyboardButton(text="ГРП-Гb11", callback_data="grp_gb11")
        ustip_curs1_turu = types.InlineKeyboardButton(text="ГРП-Гbv11", callback_data="grp_gbv11")
        ustip_curs1_up = types.InlineKeyboardButton(text="ГРП-Гbvs11", callback_data="grp_gbvs11")
        ustip_curs1_au = types.InlineKeyboardButton(text="УГП-Гb11", callback_data="ugp_gb11")
        backbutton_ustip_curs1 = types.InlineKeyboardButton(text="Назад", callback_data="ustip")
        key_ustip_curs1.add(ustip_curs1_bu, ustip_curs1_turu, ustip_curs1_up, ustip_curs1_au, backbutton_ustip_curs1)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_ustip_curs1)

    if call.data == "ustip_curs2":
        key_ustip_curs2 = types.InlineKeyboardMarkup(row_width=2)
        ustip_curs2_bu = types.InlineKeyboardButton(text="ГРП-Гb21", callback_data="grp_gb21")
        ustip_curs2_turu = types.InlineKeyboardButton(text="ГРП-Гbv21", callback_data="grp_gbv21")
        ustip_curs2_up = types.InlineKeyboardButton(text="ГРП-Гbvs21", callback_data="ugp_gb21")
        ustip_curs2_au = types.InlineKeyboardButton(text="УГП-Гb21", callback_data="ugp_gb21")
        backbutton_ustip_curs2 = types.InlineKeyboardButton(text="Назад", callback_data="ustip")
        key_ustip_curs2.add(ustip_curs2_bu, ustip_curs2_turu, ustip_curs2_up, ustip_curs2_au, backbutton_ustip_curs2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_ustip_curs2)

    if call.data == "ustip_curs3":
        key_ustip_curs3 = types.InlineKeyboardMarkup(row_width=2)
        ustip_curs3_bu = types.InlineKeyboardButton(text="ГРП-Гb31", callback_data="grp_gb31")
        ustip_curs3_turu = types.InlineKeyboardButton(text="ГРП-Гbv31", callback_data="grp_gbv31")
        ustip_curs3_up = types.InlineKeyboardButton(text="ГРП-Гbvs31", callback_data="ugp_gb31")
        ustip_curs3_au = types.InlineKeyboardButton(text="УГП-Гb31", callback_data="ugp_gb31")
        backbutton_ustip_curs3 = types.InlineKeyboardButton(text="Назад", callback_data="ustip")
        key_ustip_curs3.add(ustip_curs3_bu, ustip_curs3_turu, ustip_curs3_up, ustip_curs3_au, backbutton_ustip_curs3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_ustip_curs3)

    if call.data == "ustip_curs4":
        key_ustip_curs4 = types.InlineKeyboardMarkup(row_width=2)
        ustip_curs4_bu = types.InlineKeyboardButton(text="ГРП-Гb41", callback_data="grp_gb41")
        ustip_curs4_turu = types.InlineKeyboardButton(text="ГРП-Гbv41", callback_data="grp_gbv41")
        ustip_curs4_up = types.InlineKeyboardButton(text="ГРП-Гbvs41", callback_data="ugp_gb41")
        ustip_curs4_au = types.InlineKeyboardButton(text="УГП-Гb41", callback_data="ugp_gb41")
        backbutton_ustip_curs4 = types.InlineKeyboardButton(text="Назад", callback_data="ustip")
        key_ustip_curs4.add(ustip_curs4_up, ustip_curs4_au, backbutton_ustip_curs4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_ustip_curs4)
# Конец блока с ФЭСиП




   # elif call.data == "second":
    #    keyboard = types.InlineKeyboardMarkup()
     #   rele1 = types.InlineKeyboardButton(text="another layer", callback_data="gg")
      #  backbutton = types.InlineKeyboardButton(text="back", callback_data="mainmenu")
       # keyboard.add(rele1,backbutton)
        #bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="replaced text",reply_markup=keyboard)

#Ответы на запросы

    elif call.data == 'fasip_curs5':
        bot.send_message(call.message.chat.id, 'Извините, групп не найдено')
    elif call.data == 'ftt_curs5':
        bot.send_message(call.message.chat.id, 'Извините, групп не найдено')
    elif call.data == 'ustip_curs5':
        bot.send_message(call.message.chat.id, 'Извините, групп не найдено')
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
        bot.send_message(call.message.chat.id, 'Занятий не найдено')
    elif call.data == '6':
        bot.send_message(call.message.chat.id, 'Выполнил другое третье')
        bot.send_sticker(call.message.chat.id,'CAACAgIAAxkBAAECNwVggXmMsdcotss8NyZOlTWt2PwbVgACDcgBAAFji0YM5b2ONofFcO4fBA')


#if __name__ == "__main__":
bot.polling(none_stop=True)
import telebot
from telebot import types
import sqlite3
from datetime import datetime
from config import token
from loguru import logger
from time import sleep
import re

logger.add("bot_main.log", format="{time} {level} {message}", level="DEBUG", rotation="10 MB", compression="zip")

#ФТТ
from rasp import apa_tb11_str, apa_tb21_str, apa_tb31_str, apa_tb41_str, apm_tb11_str, apm_tb21_str, apm_tb31_str, apm_tb41_str
from rasp import bjt_tb11_str, bjt_tb21_str, bjt_tb31_str, bjt_tb41_str, ikts_tb11_str, ikts_tb21_str, ikts_tb31_str, ikts_tb41_str
from rasp import ist_tb11_str, ist_tb21_str, ist_tb31_str, ist_tb41_str, obd_tb11_str, obd_tb21_str, obd_tb31_str, obd_tb41_str
#ФЭСиП
from rasp import bu_ab11_str, bu_ab21_str, bu_ab31_str, turu_ab11_str, turu_ab21_str, turu_ab31_str
from rasp import up_ab11_str, up_ab21_str, up_ab31_str, up_ab41_str, au_ab11_str, au_ab21_str, au_ab31_str, au_ab41_str
#ЮСТиП
from rasp import grp_gb11_str, grp_gb21_str, grp_gb31_str, grp_gb41_str, grp_gbv11_str, grp_gbv21_str, grp_gbv31_str, grp_gbv41_str
from rasp import grp_gbvs11_str, grp_gbvs21_str, grp_gbvs31_str, grp_gbvs41_str, ugp_gb11_str, ugp_gb21_str, ugp_gb31_str, ugp_gb41_str, test_str

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
   try:
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Получить расписание')
    keyboard.row('Поиск аудитории')
    keyboard.row('Справочник', 'Помощь')
    bot.send_message(message.chat.id, 'Скорее выбирай раздел в Главном меню – я знаю много интересного про институт!', reply_markup=keyboard)
    logger.info("Подключился к боту ID=" + str(message.chat.id))
    #Сбор id-чатов:
    msgt = str(message.chat.id)
    base = sqlite3.connect('users.db')
    cur = base.cursor()

    base.execute('CREATE TABLE IF NOT EXISTS {}(chat_id PRIMARY KEY)'.format('bot_users'))
    base.commit()
    cur.execute('INSERT INTO bot_users VALUES(?);', (msgt,))
    base.commit()

   except:
    logger.error("Перезапускает бота ID=" + str(message.chat.id))

@bot.message_handler(commands=['help', 'info'])
def send_info(message):
   try:
    bot.send_message(message.chat.id, '💬Информационный раздел \n\nБаза данных с раписанием обновляется раз в 6 часов.\n\nОзнакомиться с базой аудиторий можно на сайте: https://isoipbot.ru/aud/  \n\nАвтор бота: Токарев Роман (@romitsu) \n\nВ случае возникновения ошибок, просим сообщать нам по адресу help@isoipbot.ru (обязательно укажите свой чат ID). \n\nВаш чат ID:\n' + str(message.chat.id))
    logger.info("Вызвал команду /help или /info ID=" + str(message.chat.id))
   except:
    logger.error("Ошибка в send_info ID=" + str(message.chat.id))

@bot.message_handler(commands=['nanoit'])
def mess(message):
   try:
    logger.info("Старт массовой отправки сообщений ID=" + str(message.chat.id))
    base = sqlite3.connect('users.db')
    cur = base.cursor()
    a_spm = cur.execute('''SELECT * FROM bot_users''')
    b_spm = a_spm.fetchall()
    spm_list = []
    for x_spm in b_spm:
        spm_list.append(' | '.join(x_spm))
    spm_str = ' '.join(spm_list)
    base.close()
    for user in spm_str.split():
        bot.send_message(user, message.text[message.text.find(' '):])
   except:
       logger.error("Ошибка массовой отправки сообщений ID=" + str(message.chat.id))

@bot.message_handler(content_types=["text"])
def any_msg(message):
   try:
    if message.text.lower() == 'получить расписание':
        keyrasp = types.InlineKeyboardMarkup(row_width=3)
        ftt_button = types.InlineKeyboardButton(text="ФТТ", callback_data="ftt")
        fasip_button = types.InlineKeyboardButton(text="ФЭСиП", callback_data="fasip")
        ustip_button = types.InlineKeyboardButton(text="ЮСТиП", callback_data="ustip")
        keyrasp.add(ftt_button, fasip_button, ustip_button)
        bot.send_message(message.chat.id, "Выберите свой факультет:", reply_markup=keyrasp)
        logger.info("Вызвал меню (получить расписание_1) ID=" + str(message.chat.id))
    elif message.text.lower() == 'справочник':
        keyinfo = types.InlineKeyboardMarkup(row_width=1)
        teacher_button = types.InlineKeyboardButton(text="Поиск преподавателя", callback_data="teacher")
        docs_button = types.InlineKeyboardButton(text="Загрузка документов", callback_data="docs")
        keyinfo.add(teacher_button, docs_button)
        bot.send_message(message.chat.id, "Выберите необходимый пункт:", reply_markup=keyinfo)
        logger.info("Вызвал (справочник_1) ID=" + str(message.chat.id))
    elif message.text.lower() == 'поиск аудитории':
        bot.send_message(message.chat.id, 'Напишите номер необходимой аудитории в чат\nНапример: 2139\n\nПожалуйста, соблюдайте масочный режим')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECOwxgheCnp0hu1296--sN16O7LdrAyAACC8gBAAFji0YMVs1sFXX6JcgfBA')
        logger.info("Вызвал (поиск аудитории_1) ID=" + str(message.chat.id))
    elif message.text.lower() == 'помощь':
        bot.send_message(message.chat.id,'💬Информационный раздел \n\nБаза данных с раписанием обновляется раз в 6 часов.\n\nОзнакомиться с базой аудиторий можно на сайте: https://isoipbot.ru/aud/  \n\nАвтор бота: Токарев Роман (@romitsu) \n\nВ случае возникновения ошибок, просим сообщать нам по адресу help@isoipbot.ru (обязательно укажите свой чат ID). \n\nВаш чат ID:\n' + str(message.chat.id))
        logger.info("Вызвал (помощь_1) ID=" + str(message.chat.id))
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
    elif message.text.lower() == 'русляков':
        img_ruslyakov = "https://www.sssu.ru/portals/0/ftt/k2.jpg"
        text_ruslyakov  = "Русляков Дмитрий Викторович \nдекан факультета «Техника и технологии» \nканд. техн. наук, доцент"
        bot.send_message(message.chat.id, f'{text_ruslyakov}\n{img_ruslyakov}')
    # Обработка поиска аудиторий
    # 1 корпус, 2 корпус, двор, 1 этаж
    elif message.text.lower() == '1101':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1101-05-15')
    elif message.text.lower() == '1102':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1102-05-15')
    elif message.text.lower() == '1103':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1103-ab-05-15')
    elif message.text.lower() == '1103а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1103-ab-05-15')
    elif message.text.lower() == '1103б':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1103-ab-05-15')
    elif message.text.lower() == '1104':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1104-05-15')
    elif message.text.lower() == '1105':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1105-05-15')			
    elif message.text.lower() == '1106':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1106-05-15')
    elif message.text.lower() == '1106б':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1106b-05-15')
    elif message.text.lower() == '1108':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1108-05-15')
    elif message.text.lower() == '1109':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1109-05-15')
    elif message.text.lower() == '1110':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1110-05-15')
    elif message.text.lower() == '1111':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1111-05-15')
    elif message.text.lower() == '1112':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1112-05-15')
    elif message.text.lower() == '1113':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1113-05-15')
    elif message.text.lower() == '1114':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1114-05-15')
    elif message.text.lower() == '1114а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1114a-05-15')
    elif message.text.lower() == '1115':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1115-05-15')	
    elif message.text.lower() == '1116':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1116-05-15')
    elif message.text.lower() == '1117':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1117-05-15')
    #Двор
    elif message.text.lower() == '2109':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2109-05-16')
    elif message.text.lower() == '2110':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2110-05-16')
    elif message.text.lower() == '2116':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2116-2116a-2116b-2117-05-16')
    elif message.text.lower() == '2116а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2116-2116a-2116b-2117-05-16')
    elif message.text.lower() == '2116б':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2116-2116a-2116b-2117-05-16')
    elif message.text.lower() == '2117':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2116-2116a-2116b-2117-05-16')
    elif message.text.lower() == '2118':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2118-05-16')
    #2корпус 1 эт
    elif message.text.lower() == '2135':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2135-05-16')
    elif message.text.lower() == '2136':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2136-05-16')
    elif message.text.lower() == '2137':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2137-05-16')
    elif message.text.lower() == '2138':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2138-05-16')
    elif message.text.lower() == '2139':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2139-05-16')
    elif message.text.lower() == '2140':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2140-05-16')
    elif message.text.lower() == '2141':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2141-05-16')
    elif message.text.lower() == '2142':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2142-05-16')
    elif message.text.lower() == '2143':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2143-05-16')
    elif message.text.lower() == '2144':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2144-05-16')
    elif message.text.lower() == '2156':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2156-2155-2151-05-16')
    elif message.text.lower() == '2155':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2156-2155-2151-05-16')
    elif message.text.lower() == '2151':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2156-2155-2151-05-16')
    elif message.text.lower() == '2159':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2159-05-17')
    elif message.text.lower() == '2158':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2158-2158a-2158b-2158v-2158g-05-17')
    elif message.text.lower() == '2158а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2158-2158a-2158b-2158v-2158g-05-17')
    elif message.text.lower() == '2158б':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2158-2158a-2158b-2158v-2158g-05-17')
    elif message.text.lower() == '2158в':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2158-2158a-2158b-2158v-2158g-05-17')
    elif message.text.lower() == '2158г':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2158-2158a-2158b-2158v-2158g-05-17')
    elif message.text.lower() == '2261':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2261-2262-2263-2264-2265-05-17')
    elif message.text.lower() == '2262':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2261-2262-2263-2264-2265-05-17')
    elif message.text.lower() == '2263':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2261-2262-2263-2264-2265-05-17')
    elif message.text.lower() == '2265':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2261-2262-2263-2264-2265-05-17')
    elif message.text.lower() == '2265':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2261-2262-2263-2264-2265-05-17')
    elif message.text.lower() == '2161':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2161-05-17')
    elif message.text.lower() == '2166':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2166-a-b-v-05-17')
    elif message.text.lower() == '2166а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2166-a-b-v-05-17')
    elif message.text.lower() == '2166б':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2166-a-b-v-05-17')
    elif message.text.lower() == '2166в':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2166-a-b-v-05-17')
    elif message.text.lower() == '2166г':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2166g-05-17')
    elif message.text.lower() == '2167':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2167-05-17')
    elif message.text.lower() == '2169':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2168-2169-2268-2269-05-17')
    elif message.text.lower() == '2168':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2168-2169-2268-2269-05-17')
    elif message.text.lower() == '2269':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2168-2169-2268-2269-05-17')
    elif message.text.lower() == '2268':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2168-2169-2268-2269-05-17')
    elif message.text.lower() == '2268а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2168-2169-2268-2269-05-17')
    elif message.text.lower() == '2268б':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2168-2169-2268-2269-05-17')
    #1 корпус, 2 этаж
    elif message.text.lower() == '1201':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1201-05-25')
    elif message.text.lower() == '1201а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1201a-05-26')
    elif message.text.lower() == '1202':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1202-05-26')
    elif message.text.lower() == '1203':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1203-05-26')
    elif message.text.lower() == '1204':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1204-05-26')
    elif message.text.lower() == '1205':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1205-05-26')   
    elif message.text.lower() == '1206':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-1206-1207-05-26')   
    elif message.text.lower() == '1207':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-1206-1207-05-26')   
    elif message.text.lower() == '1208':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-1208-1209-05-26')   
    elif message.text.lower() == '1209':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-1208-1209-05-26')   
    elif message.text.lower() == '1210':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1210-05-26')   
    elif message.text.lower() == '1211':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1211-05-26')
    elif message.text.lower() == '1212':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1212-05-26')   
    elif message.text.lower() == '1213':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1213-05-26')   
    elif message.text.lower() == '1214':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1214-05-26')   
    elif message.text.lower() == '1215':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1215-05-26')       
    elif message.text.lower() == '1216':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1216-05-26') 
    elif message.text.lower() == '1216а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1216a-05-26') 
    elif message.text.lower() == '1217':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1217-05-26') 
    elif message.text.lower() == '1218':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-1218-1219-05-26')
    elif message.text.lower() == '1219':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-1218-1219-05-26')
    elif message.text.lower() == '1220а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1220-a-b-05-26') 
    elif message.text.lower() == '1220б':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1220-a-b-05-26') 
    elif message.text.lower() == '1221':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1221-05-26')                                                                    
    #1 корпус, 3 этаж
    elif message.text.lower() == '1301':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1301-05-26')
    elif message.text.lower() == '1302':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1302-05-26')
    elif message.text.lower() == '1302а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1302a-05-26')
    elif message.text.lower() == '1303':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1303-05-26')
    elif message.text.lower() == '1304':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1304-05-26')
    elif message.text.lower() == '1305':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-1305-1306-05-26')
    elif message.text.lower() == '1306':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-1305-1306-05-26-2')
    elif message.text.lower() == '1307':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1307-05-26')
    elif message.text.lower() == '1308':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1308-05-26')
    elif message.text.lower() == '1309':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1309-05-26') 
    elif message.text.lower() == '1310':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1310-05-26')
    elif message.text.lower() == '1311':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1311-05-26')
    elif message.text.lower() == '1312':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1312-05-26')
    elif message.text.lower() == '1313':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1313-05-26')
    elif message.text.lower() == '1314':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1314-05-26')
    elif message.text.lower() == '1315':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1315-05-26')
    elif message.text.lower() == '1316':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1316-05-26')
    elif message.text.lower() == '1317':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1317-05-26')
    elif message.text.lower() == '1318':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1318-05-26')      
    #1 корпус, 4 этаж
    elif message.text.lower() == '1401':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1401-06-14')
    elif message.text.lower() == '1401б':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1401b-06-14')
    elif message.text.lower() == '1401а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1401a-06-14')
    elif message.text.lower() == '1402':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1402-06-14')
    elif message.text.lower() == '1402а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1402a-06-14')
    elif message.text.lower() == '1403':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1403-06-14')
    elif message.text.lower() == '1404':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1404-06-14')
    elif message.text.lower() == '1405':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1405-06-14')
    elif message.text.lower() == '1406':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1406-06-14')
    elif message.text.lower() == '1407':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1407-06-14')
    elif message.text.lower() == '1408':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1408-06-14')
    elif message.text.lower() == '1409':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1409-06-14')
    elif message.text.lower() == '1410':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1410-06-14')
    elif message.text.lower() == '1410а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1410a-06-14')
    elif message.text.lower() == '1411':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1411-06-14')
    elif message.text.lower() == '1412':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1412-06-14')
    elif message.text.lower() == '1413':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1413-06-14')
    elif message.text.lower() == '1414':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1414-06-14')
    elif message.text.lower() == '1415':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1415-06-14')
    elif message.text.lower() == '1415б':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1415b-06-14')
    elif message.text.lower() == '1416':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1416-06-14')
    elif message.text.lower() == '1417':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1417-06-14')
    elif message.text.lower() == '1417а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1417a-06-14')
    elif message.text.lower() == '1418':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-1418-06-14')
    #2 корпус, 2 этаж
    elif message.text.lower() == '2235':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2235-06-15')
    elif message.text.lower() == '2236':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2236-06-15')
    elif message.text.lower() == '2237':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2237-06-15')
    elif message.text.lower() == '2239':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2239-2240-2241-06-15')
    elif message.text.lower() == '2240':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2239-2240-2241-06-15')
    elif message.text.lower() == '2241':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2239-2240-2241-06-15')
    elif message.text.lower() == '2242':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2242-2243-06-15')
    elif message.text.lower() == '2243':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2242-2243-06-15')
    elif message.text.lower() == '2244':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2244-06-15')
    elif message.text.lower() == '2245':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2245-06-15')
    elif message.text.lower() == '2246':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2246-06-15')
    elif message.text.lower() == '2247':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2247-06-15')
    elif message.text.lower() == '2248':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2248-06-15')
    elif message.text.lower() == '2249':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2249-06-15')
    elif message.text.lower() == '2249а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2249-06-15')
    elif message.text.lower() == '2250':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2250-06-15')
    elif message.text.lower() == '2250а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2250-06-15')
    elif message.text.lower() == '2251':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2251-06-15')
    elif message.text.lower() == '2252':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2252-06-15')
    elif message.text.lower() == '2253':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2253-06-15')
    elif message.text.lower() == '2254':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2254-06-15')
    elif message.text.lower() == '2255':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2255-2256-06-15')
    elif message.text.lower() == '2256':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditorii-2255-2256-06-15')
    #2 корпус, 3 этаж
    elif message.text.lower() == '2330':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2330-06-15')
    elif message.text.lower() == '2331':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2331-06-15')
    elif message.text.lower() == '2332':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2332-06-15')
    elif message.text.lower() == '2333':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2333-06-15')
    elif message.text.lower() == '2333а':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2333a-06-15')
    elif message.text.lower() == '2335':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2335-06-15')
    elif message.text.lower() == '2336':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2336-06-15')
    elif message.text.lower() == '2337':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2337-06-15')
    elif message.text.lower() == '2338':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2338-06-15')
    elif message.text.lower() == '2339':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2339-06-15')
    elif message.text.lower() == '2340':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2340-06-15')
    elif message.text.lower() == '2341':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2341-06-15')
    elif message.text.lower() == '2342':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2342-06-15')
    elif message.text.lower() == '2343':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2343-06-15')
    elif message.text.lower() == '2344':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2344-06-15')
    elif message.text.lower() == '2345':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2345-06-15-2')
    elif message.text.lower() == '2346':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2346-06-15')
    elif message.text.lower() == '2347':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2347-06-15')
    elif message.text.lower() == '2348':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2348-06-15')
    elif message.text.lower() == '2349':
        bot.send_message(message.chat.id, 'https://telegra.ph/Auditoriya-2349-06-15')
    # Дополнительные ответы  
    elif message.text.lower() == 'как сдать сессию?':
        bot.send_message(message.chat.id, 'Я не знаю, прости :(')
    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Ещё раз привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока!')
    elif message.text.lower() == 'тест':
        bot.send_message(message.chat.id, 'Тестовая демонстрация вывода расписания')
        bot.send_message(message.chat.id, test_str)
    else:
        bot.send_message(message.chat.id, 'Ничего не понятно, но очень интересно. \nПопробуйте команду /help')
        logger.info("Вызвал неизвестное сообщение ID=" + str(message.chat.id))
   except:
    logger.error("Ошибка в any_msg ID=" + str(message.chat.id))
		
#keyboardmain
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
   try:
    if call.data == "mainmenu":
        keyrasp = types.InlineKeyboardMarkup(row_width=3)
        ftt_button = types.InlineKeyboardButton(text="ФТТ", callback_data="ftt")
        fasip_button = types.InlineKeyboardButton(text="ФЭСиП", callback_data="fasip")
        ustip_button = types.InlineKeyboardButton(text="ЮСТиП", callback_data="ustip")
        keyrasp.add(ftt_button, fasip_button, ustip_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите свой факультет:",reply_markup=keyrasp)
        logger.info("Вызвал меню (выбор факультета_2) ID=" + str(call.message.chat.id))
    elif call.data == "maininfo":
        keyinfo = types.InlineKeyboardMarkup(row_width=1)
        teacher_button = types.InlineKeyboardButton(text="Поиск преподавателя", callback_data="teacher")
        docs_button = types.InlineKeyboardButton(text="Загрузка документов", callback_data="docs")
        keyinfo.add(teacher_button, docs_button)
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Выберите необходимый пункт:",reply_markup=keyinfo)
        logger.info("Вызвал меню (справочное_2) ID=" + str(call.message.chat.id))
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
        logger.info("Вызвал меню (документы_2) ID=" + str(call.message.chat.id))
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
        key_ustip_curs4.add(ustip_curs4_up, ustip_curs4_au, backbutton_ustip_curs4, ustip_curs4_bu, ustip_curs4_turu)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите свою группу:", reply_markup=key_ustip_curs4)
# Конец блока с ФЭСиП

    elif call.data == 'fasip_curs5':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Извините, групп не найдено')

    elif call.data == 'ftt_curs5':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Извините, групп не найдено')

    elif call.data == 'ustip_curs5':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Извините, групп не найдено')
    #Факультет ФТТ
    elif call.data == 'apa_tb11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ЭПА-Тb11')
        bot.send_message(call.message.chat.id, apa_tb11_str)

    elif call.data == 'apa_tb21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ЭПА-Тb21')
        bot.send_message(call.message.chat.id, apa_tb21_str)

    elif call.data == 'apa_tb31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ЭПА-Тb31')
        bot.send_message(call.message.chat.id, apa_tb31_str)

    elif call.data == 'apa_tb41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ЭПА-Тb41')
        bot.send_message(call.message.chat.id, apa_tb41_str)

    elif call.data == 'apm_tb11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание АПМ-Тb11')
        bot.send_message(call.message.chat.id, apm_tb11_str)

    elif call.data == 'apm_tb21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание АПМ-Тb21')
        bot.send_message(call.message.chat.id, apm_tb21_str)

    elif call.data == 'apm_tb31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание АПМ-Тb31')
        bot.send_message(call.message.chat.id, apm_tb31_str)

    elif call.data == 'apm_tb41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание АПМ-Тb41')
        bot.send_message(call.message.chat.id, apm_tb41_str)

    elif call.data == 'bjt_tb11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание БЖТ-Тb11')
        bot.send_message(call.message.chat.id, bjt_tb11_str)

    elif call.data == 'bjt_tb21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание БЖТ-Тb21')
        bot.send_message(call.message.chat.id, bjt_tb21_str)

    elif call.data == 'bjt_tb31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание БЖТ-Тb31')
        bot.send_message(call.message.chat.id, bjt_tb31_str)

    elif call.data == 'bjt_tb41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание БЖТ-Тb41')
        bot.send_message(call.message.chat.id, bjt_tb41_str)

    elif call.data == 'ikts_tb11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ИКТС-Тb11')
        bot.send_message(call.message.chat.id, ikts_tb11_str)

    elif call.data == 'ikts_tb21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ИКТС-Тb21')
        bot.send_message(call.message.chat.id, ikts_tb21_str)

    elif call.data == 'ikts_tb31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ИКТС-Тb31')
        bot.send_message(call.message.chat.id, ikts_tb31_str)

    elif call.data == 'ikts_tb41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ИКТС-Тb41')
        bot.send_message(call.message.chat.id, ikts_tb41_str)

    elif call.data == 'ist_tb11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ИСТ-Тb11')
        base = sqlite3.connect('rasp.db')
        cur = base.cursor()
        kuka = cur.execute('''SELECT * FROM ist_tb11''')

        bot.send_message(call.message.chat.id, kuka)

    elif call.data == 'ist_tb21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ИСТ-Тb21')
        bot.send_message(call.message.chat.id, ist_tb21_str)

    elif call.data == 'ist_tb31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ИСТ-Тb31')
        bot.send_message(call.message.chat.id, ist_tb31_str)

    elif call.data == 'ist_tb41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ИСТ-Тb41')
        bot.send_message(call.message.chat.id, ist_tb41_str)

    elif call.data == 'obd_tb11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ОБД-Тb11')
        bot.send_message(call.message.chat.id, obd_tb11_str)

    elif call.data == 'obd_tb21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ОБД-Тb21')
        bot.send_message(call.message.chat.id, obd_tb21_str)

    elif call.data == 'obd_tb31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ОБД-Тb31')
        bot.send_message(call.message.chat.id, obd_tb31_str)

    elif call.data == 'obd_tb41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ОБД-Тb41')
        bot.send_message(call.message.chat.id, obd_tb41_str)
    # Факультет ФЭСиП
    elif call.data == 'bu_ab11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание БУ-Эb11')
        bot.send_message(call.message.chat.id, bu_ab11_str)

    elif call.data == 'bu_ab21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание БУ-Эb21')
        bot.send_message(call.message.chat.id, bu_ab21_str)

    elif call.data == 'bu_ab31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание БУ-Эb31')
        bot.send_message(call.message.chat.id, bu_ab31_str)

    elif call.data == 'turu_ab11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ТУРУ-Эb11')
        bot.send_message(call.message.chat.id, turu_ab11_str)

    elif call.data == 'turu_ab21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ТУРУ-Эb21')
        bot.send_message(call.message.chat.id, turu_ab21_str)

    elif call.data == 'turu_ab31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ТУРУ-Эb31')
        bot.send_message(call.message.chat.id, turu_ab31_str)

    elif call.data == 'up_ab11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание УП-Эb11')
        bot.send_message(call.message.chat.id, up_ab11_str)

    elif call.data == 'up_ab21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание УП-Эb21')
        bot.send_message(call.message.chat.id, up_ab21_str)

    elif call.data == 'up_ab31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание УП-Эb31')
        bot.send_message(call.message.chat.id, up_ab31_str)

    elif call.data == 'up_ab41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание УП-Эb41')
        bot.send_message(call.message.chat.id, up_ab41_str)

    elif call.data == 'au_ab11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ЭУ-Эb11')
        bot.send_message(call.message.chat.id, au_ab11_str)

    elif call.data == 'au_ab21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ЭУ-Эb21')
        bot.send_message(call.message.chat.id, au_ab21_str)

    elif call.data == 'au_ab31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ЭУ-Эb31')
        bot.send_message(call.message.chat.id, au_ab31_str)

    elif call.data == 'au_ab41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ЭУ-Эb41')
        bot.send_message(call.message.chat.id, au_ab41_str)
    #ЮСТиП
    elif call.data == 'grp_gb11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гb11')
        bot.send_message(call.message.chat.id, grp_gb11_str)

    elif call.data == 'grp_gb21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гb21')
        bot.send_message(call.message.chat.id, grp_gb21_str)

    elif call.data == 'grp_gb31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гb31')
        bot.send_message(call.message.chat.id, grp_gb31_str)

    elif call.data == 'grp_gb41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гb41')
        bot.send_message(call.message.chat.id, grp_gb41_str)

    elif call.data == 'grp_gbv11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbv11')
        bot.send_message(call.message.chat.id, grp_gbv11_str)

    elif call.data == 'grp_gbv21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbv21')
        bot.send_message(call.message.chat.id, grp_gbv21_str)

    elif call.data == 'grp_gbv31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbv31')
        bot.send_message(call.message.chat.id, grp_gbv31_str)

    elif call.data == 'grp_gbv41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbv41')
        bot.send_message(call.message.chat.id, grp_gbv41_str)

    elif call.data == 'grp_gbvs11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbvs11')
        bot.send_message(call.message.chat.id, grp_gbvs11_str)

    elif call.data == 'grp_gbvs21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbvs21')
        bot.send_message(call.message.chat.id, grp_gbvs21_str)

    elif call.data == 'grp_gbvs31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbvs31')
        bot.send_message(call.message.chat.id, grp_gbvs31_str)

    elif call.data == 'grp_gbvs41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание ГРП-Гbvs41')
        bot.send_message(call.message.chat.id, grp_gbvs41_str)

    elif call.data == 'ugp_gb11':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание УГП-Гb11')
        bot.send_message(call.message.chat.id, ugp_gb11_str)

    elif call.data == 'ugp_gb21':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание УГП-Гb21')
        bot.send_message(call.message.chat.id, ugp_gb21_str)

    elif call.data == 'ugp_gb31':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание УГП-Гb31')
        bot.send_message(call.message.chat.id, ugp_gb31_str)

    elif call.data == 'ugp_gb41':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Расписание УГП-Гb41')
        bot.send_message(call.message.chat.id, ugp_gb41_str)

    elif call.data == 'teacher':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Пожалуйста, напишите фамилию преподавателя\nНапример: Попов ')
    # Документы:
    elif call.data == 'docs1':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Заявка на выдачу справки-вызова ФТТ')
        file1 = open('docs/ftt.docx', 'rb')
        bot.send_document(call.message.chat.id, file1)
        logger.info("Пользователь выбрал 1 документ ID=" + str(call.message.chat.id))

    elif call.data == 'docs2':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Заявка на выдачу справки-вызова ФЭСиП')
        file2 = open('docs/fasip.doc', 'rb')
        bot.send_document(call.message.chat.id, file2)
        logger.info("Пользователь выбрал 2 документ ID=" + str(call.message.chat.id))

    elif call.data == 'docs3':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Заявка на выдачу справки-вызова ФЮСТиП')
        file3 = open('docs/ustip.doc', 'rb')
        bot.send_document(call.message.chat.id, file3)
        logger.info("Пользователь выбрал 3 документ ID=" + str(call.message.chat.id))

    elif call.data == 'docs4':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Правила оформления письменных работ')
        file4 = open('docs/242pr.pdf', 'rb')
        bot.send_document(call.message.chat.id, file4)
        logger.info("Пользователь выбрал 4 документ ID=" + str(call.message.chat.id))

    elif call.data == 'docs5':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Правила применения шаблонов оформления')
        file5 = open('docs/242sh.pdf', 'rb')
        bot.send_document(call.message.chat.id, file5)
        logger.info("Пользователь выбрал 5 документ ID=" + str(call.message.chat.id))

    elif call.data == 'docs6':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, 'Список задолжностей')
        file6 = open('docs/dolg.doc', 'rb')
        bot.send_document(call.message.chat.id, file6)
        logger.info("Пользователь выбрал 6 документ ID=" + str(call.message.chat.id))
   except:
       logger.error("Ошибка в callback_inline ID=" + str(call.message.chat.id))


#Проверка запусков
current_datetime = datetime.now()
print(current_datetime)

base = sqlite3.connect('starts.db')
cur = base.cursor()

base.execute('CREATE TABLE IF NOT EXISTS {}(info_starts)'.format('table_starts'))
base.commit()

cur.execute('INSERT INTO table_starts VALUES(?);', (current_datetime,))
base.commit()
#Проверка запусков

bot.polling(none_stop=True, interval=0)

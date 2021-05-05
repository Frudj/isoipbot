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
    bot.send_message(message.chat.id, 'Добро пожаловать в стартовое меню!', reply_markup=keyboard)
    if not str(message.chat.id) in joinedUser:
        file = open('users.txt', 'a')
        file.write(str(message.chat.id) + '\n')
        file.close()

@bot.message_handler(commands=['spm'])
def mess(message):
    for user in joinedUser:
        bot.send_message(user, message.text[message.text.find(' '):])
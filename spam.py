joiFile = open("id.txt", "r")
joiUsers = set()
for line in joiFile:
    joiUsers.add(line.strip())
joiFile.close()

#commands start
def startJoin(message):
    if not str(message.chat.id) in joiUsers:
        joiFile = open("id.txt", "a")
        joiFile.write(str(message.chat.id) + "\n")
        joiUsers.add(message.chat.id)

@bot.message_handler(commands=['special'])
def mess(message):
    for user in joiUsers:
        bot.send_message(user, message.text[message.text.find(' '):])
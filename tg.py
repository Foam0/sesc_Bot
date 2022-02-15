import telebot
from IS_trying_to_reg import is_trying
from next import next
from rasp import rasp
from registration import reg

myid = 694191338
bot = telebot.TeleBot('token main')
debug = telebot.TeleBot('token debug')


def help(message, bot):
    bot.send_message(message.from_user.id, "/tomorrow - расписание на завтра\n"
                                           "/today - расписание на сегодня\n"
                                           "/next - следующие начало урока + кабинет + учитель\n"
                                           "/reg - Регистрация, без неё никуда")


def time(message, bot):
    bot.send_message(message.from_user.id, "1 урок	9:00	9:40\n"
                                           "2 урок	9:50	10:30\n"
                                           "3 урок	10:45	11:25\n"
                                           "4 урок	11:40	12:20\n"
                                           "5 урок	12:35	13:15\n"
                                           "6 урок	13:35	14:15\n"
                                           "7 урок	14:35	15:15"
                     )


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    try:
        debug.send_message(myid, str(message.from_user.username + ':' + str(
            message.from_user.full_name) + ':' + str(message.from_user.id) + ':' + message.text))
    except:
        try:
            debug.send_message(myid, (
                    str(message.from_user.full_name) + ':' + str(message.from_user.id) + ':' + message.text))
        except:
            print("Error")
    if message.text=="/time":
        time(message,bot)
    elif message.text == "/tomorrow" or message.text == '/today':
        rasp(message, bot)
    elif message.text == "/help" or message.text == '/start':
        help(message, bot)
    elif message.text == "/next":
        next(message, bot)
    elif message.text == "/reg":
        reg(message, bot, state=1)
    else:
        if is_trying(message.from_user.id):
            reg(message, bot, state=2)
        else:
            bot.send_message(message.from_user.id,
                             "ниче не понятно напиши /help или разработчику @foam0")


while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        print("error")
        debug.send_message(myid, str("error"))
# pyinstaller --add-data "people.txt;." --add-data "Trying to reg.txt;." tg.py
# pyinstaller  tg.py

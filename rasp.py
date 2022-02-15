import datetime

from ASK_GROUP import group
from get import get


def rasp(message, bot):
    group0 = group(message.from_user.id)
    if group0=="NO":
        bot.send_message(message.from_user.id, "напиши /reg")
        return 0
    if message.text == "/tomorrow":
        if (datetime.datetime.today().weekday() + 2) % 7 == 0:
            bot.send_message(message.from_user.id, "Воскресенье")
            return 0
        s = get((datetime.datetime.today().weekday() + 2) % 7,group0)
    else:
        if (datetime.datetime.today().weekday() + 1) % 7 == 0:
            bot.send_message(message.from_user.id, "Воскресенье")
            return 0
        s = get((datetime.datetime.today().weekday() + 1) % 7,group0)
    mas = ''
    for i in sorted(s.keys()):
        mas += str(i) + ')'
        for j in sorted(s[i]):
            if (j == 1 or s[i][j - 1] != s[i][j]):
                mas += str(s[i][j]["subject"]) + ' '
        mas += '\n'
    bot.send_message(message.from_user.id, mas)

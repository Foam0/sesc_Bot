from bs4 import BeautifulSoup
from requests import get
from lxml import *

def reg(message, bot, state=1):
    if state == 1:
        bot.send_message(message.from_user.id, "Введите ваш класс в формате \"8Б\"'")
        file = open("Trying to reg.txt", 'r').readlines()
        s = set()
        for i in file:
            s.add(i.rsplit('\n')[0])
        s.add(str(message.from_user.id))
        file = open("Trying to reg.txt", 'w')
        for i in s:
            print(i, file=file)
        file.close()

    else:
        x = get("https://lyceum.urfu.ru/ucheba/raspisanie-zanjatii")
        soup = BeautifulSoup(x.content, 'html.parser')
        soup = (soup.find_all("option", text=str(message.text).upper()))

        if len(soup) == 0:
            bot.send_message(message.from_user.id, "Скорее всего ваш класс уже расформирован. Можете не приходить в СУНЦ.")
        else:
            file = open("people.txt", 'r').readlines()
            s = dict()
            for i in range(len(file)):
                a = file[i].split(':')[0]
                b = file[i].split(':')[1].rsplit('\n')[0]
                s[a] = b
            s[str(message.from_user.id)] = soup[0].attrs['value']
            file = open("people.txt", 'w')
            for i in s.keys():
                print(i, ':', s[i], file=file, sep='')
            file.close()
            file = open("Trying to reg.txt", 'r').readlines()
            s = set()
            for i in file:
                s.add(i.rsplit('\n')[0])
            s.remove(str(message.from_user.id))
            file = open("Trying to reg.txt", 'w')
            for i in s:
                print(i, file=file)
            file.close()
            bot.send_message(message.from_user.id, "Успешная регистрация")
#pyinstaller -F --add-data "people.txt;." --add-data "people.txt;." tg.py


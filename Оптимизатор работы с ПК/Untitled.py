import glob
import os
from colorama import init, Fore, Back, Style
init()
import sys
import encodings
from datetime import date, time, datetime
from webbrowser import open

#Коронавирус, уйди с нашего района
from bs4 import BeautifulSoup
import requests as req

#Парсим данные по числу заболевших
def korona():
    try: #Если есть интенет
        resp = req.get("https://yandex.ru/maps/covid19?ll=58.510520%2C41.006260&z=3")
        soup = BeautifulSoup(resp.text, 'lxml')

        print(Fore.RED + 'Коронавирус - Россия')
        kor = soup.find("div", {"class": "covid-stat-view__item-value"}).text.strip()
        print('╔═════════╗')
        print('║',kor,'║')
        print('╚═════════╝')
    except: #Если нет интернета
        print(Fore.RED + 'Коронавирус - Россия')
        print('Подключите интернет для отображения статистики')

#Основной код программы
while True:
    #После каждого перезапуска, чистим окно
    os.system('cls')
    #Задаём размеры консольного окна
    os.system('mode 100, 34')
    #Модуль напоминаний на каждый день недели
    today = date.today()
    v = int(today.weekday())
    if v == 0:
        #Понедельник
        print(Style.BRIGHT + Fore.BLUE) #Цвет текста
        print('╔══════════════════════════════════════╗')
        print('║Python:                               ║')
        print('╚══════════════════════════════════════╝')

    elif v == 1:
        #Вторник
        print(Style.BRIGHT + Fore.BLUE) #Цвет текста
        print('╔══════════════════════════════════════╗')
        print('║Python:                               ║')
        print('╚══════════════════════════════════════╝')

    elif v == 2:
        #Среда
        print(Style.BRIGHT + Fore.BLUE) #Цвет текста
        print('╔══════════════════════════════════════╗')
        print('║Python:                               ║')
        print('╚══════════════════════════════════════╝')

    elif v == 3:
        #Четверг
        print(Style.BRIGHT + Fore.BLUE) #Цвет текста
        print('╔══════════════════════════════════════╗')
        print('║Python:                               ║')
        print('╚══════════════════════════════════════╝')

    elif v == 4:
        #Пятница
        print(Style.BRIGHT + Fore.BLUE) #Цвет текста
        print('╔══════════════════════════════════════╗')
        print('║Немного Python:                       ║')
        print('║SQL - 20 минут:                       ║')
        print('║HTML - 20 минут:                      ║')
        print('╚══════════════════════════════════════╝')

    elif v == 5:
        #Суббота
        print(Style.BRIGHT + Fore.BLUE) #Цвет текста
        print('╔══════════════════════════════════════╗')
        print('║Прогулки:                             ║')
        print('╚══════════════════════════════════════╝')

    elif v == 6:
        #Воскресенье
        print(Style.BRIGHT + Fore.BLUE) #Цвет текста
        print('╔══════════════════════════════════════╗')
        print('║Прогулки:                             ║')
        print('╚══════════════════════════════════════╝')

    #Заголовок программы
    print(Style.RESET_ALL +'║║║║║║║  ║║║║║║║║║║  ║║║        ║║║  ║║   ║║')
    print('║║   ║║  ║║          ║║║║      ║║║║  ║║  ║║                   ')
    print('║║   ║║  ║║          ║║  ║║  ║║  ║║  ║║ ║║                    ')
    print('║║║║║║║  ║║║║║║║║║║  ║║    ║║    ║║  ║║║║                     ')
    print('║║       ║║      ║║  ║║          ║║  ║║ ║║                    ')
    print('║║       ║║      ║║  ║║          ║║  ║║  ║║                   ')
    print('║║       ║║║║║║║║║║  ║║          ║║  ║║   ║║                  ')

    print(Style.BRIGHT + Fore.YELLOW +'==============================================')
    print('======= Оптимизатор работы: Версия 2.6 =======')
    print('==============================================')

    korona()

    print(Style.BRIGHT + Fore.RED) #Цвет текста
    print(Back.RED + Fore.WHITE + os.getcwd()) #Текущий каталог
    print(Style.RESET_ALL + Style.BRIGHT + Fore.GREEN) #Цвет текста
    #Рабочие профили
    print('╔═════════════════════════════════╗')
    print('║Какой профиль выбираем?          ║')
    print('║0. Выход:                        ║')
    print('║1. Лог версий:                   ║')
    print('║2. Учебный:                      ║')
    print('║3. Развлекательный:              ║')
    print('║4. Мои проекты                   ║')
    print('║5. Выключить компьютер:          ║')
    print('║6. Нужное:                       ║')
    print('╚═════════════════════════════════╝')

    #Блоки профилей
    a = str(input('Введите значение: '))
    if a == '0': #Выход
        print('Выход:')
        sys.exit()

    elif a == '1': #Лог версий
        os.startfile(r"mod\log\log.html")

    elif a == '2': #Учебный
        print('0. Обратно в меню: ')
        print('1. Python: ')
        print('2. SQL: ')
        print('3. HTML: ')
        print('4. C#: ')
        b = int(input ('Введите значение: '))
        if b == 0:
            print('Выход')

        elif b == 1: #Python
            #Вконтакте
            #Как скомпилировать python приложение?
            open("http://toolmark.ru/kak-skompilirovat-python-prilozhenie/")
            #Основы Python
            open("https://www.youtube.com/watch?v=vqsalStEu38&list=PLlWXhlUMyooaeSj8L8tVVbtUo0WCO4ORR&index=17")
            #GitHub
            open("https://github.com/")
            #Checkio
            open("https://checkio.org/")

        elif b == 2: #SQL
            # SQL Задачи и решения
            open("http://www.sql-tutorial.ru/ru/content.html")
            # Упражнения по SQL
            open("http://www.sql-ex.ru/learn_exercises.php")
            # Гоша Дударь
            open("https://www.youtube.com/watch?v=BfaKBs_eQXw")

        elif b == 3: #HTML
            #Справочник по HTML
            open("http://htmlbook.ru/samhtml")
            
                
        elif b == 4: # C#
            #Канал CODE BLOG - Программирование и C#
            open("https://www.youtube.com/user/admshwan/videos")
            #Плейлист C#
            open("https://www.youtube.com/playlist?list=PLIIXgDT0bKw4OmiZ9yGmShKsY0XncViZ8")

    elif a == '3': #Развлекательный
        #Хороший выбор!
        open("https://www.youtube.com/user/GoodChoiceShow/videos")
        #Новинки IT 
        open("https://www.youtube.com/user/MarozOFF/videos")
        #Saya Scarlet
        open("https://www.youtube.com/user/TheSayaScarlet/videos")
        #CORE
        open("https://www.youtube.com/user/1servicecore/videos")
        #Лёша Кластер
        open("https://www.youtube.com/user/ClusterMeerkat/videos")
        #Уютный подвальчик
        open("https://www.youtube.com/user/podval4ikshow/videos")
        #xDlate Production
        open("https://www.youtube.com/user/YogusFirst/videos")
        #Кирилл Лейфер
        open("https://www.youtube.com/user/kogdazjasdohnu/videos")
        #stalkash
        open("https://www.youtube.com/channel/UCOpm7EqPBtznEwYNNZrz1FQ/videos")
        #TEHNOGLOBE TV
        open("https://www.youtube.com/user/bulletproofzzz7o62/videos")
        #Russian Geek
        open("https://www.youtube.com/user/PxlDevil/videos")
        #Pixel_Devil Live
        open("https://www.youtube.com/user/pixeldevillive/videos")
        #hhwang - кто молодец?!
        open("https://www.youtube.com/channel/UCkJhWA2SEYbVYnE2Y2FWryA/videos")
        #Nitroxsenys
        open("https://www.youtube.com/channel/UCF3d6ZcTRBhnrNC0-cvzicw/videos")
        #Odd Tinkering
        open("https://www.youtube.com/channel/UCf_suVrG2dA5BTjJhNLwthQ/videos")

    elif a == '4': #Мои проекты
        pass

    elif a == '5': #Выключить компьютер
        os.system('shutdown /s /t 2')
        sys.exit()

    elif a == '6': #Нужное
        pass

    else:
        print('Неверное значение:')
        input('Для продолжения нажмите Enter...')
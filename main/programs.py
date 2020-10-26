import pyexcel
from datetime import timedelta, datetime, date
from .models import Car, Propusk
#from anticaptchaofficial.recaptchav2proxyless import *
from openpyxl import Workbook
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#import datetime as dt
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# #from anticaptchaofficial.imagecaptcha import *
# from PIL import Image


def handle_uploaded_file(request, file, program):
    print('program - ', program)
    if program == 'add_file_annul':
        print('handle_uploaded_file add_file_annul')
        with open('workstation/static/fileupload/' + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        print('file saved')
        all_our_annul_propuska = add_annul_propusk_to_db(file=file, request=request)
        return all_our_annul_propuska
    if program == 'add_file_our_cars':
        print('handle_uploaded_file add_file_our_cars')
        with open('workstation/static/fileupload/' + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        print('file saved')
        take_propusk_frome_allprovereno(file=file, request=request)
    if program == 'add_file_reestr_ba':
        print('handle_uploaded_file add_propusk_to_reestr_ba')
        with open('workstation/static/fileupload/' + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        print('file saved')
        add_propusk_to_reestr_ba(file=file, request=request)


def search_in_db_propusk(ser_type, ser):
    is_in = False
    try:
        print(ser)
        queryset = Propusk.objects.filter(serial_type=ser_type)
        queryset = queryset.filter(serial_num=ser)
        if queryset.exists():
            print("На {} уже есть пропуск в БД".format(ser))
            is_in = True
    except:
        is_in = False
    return is_in


def obj_search_by_car_in_db_propusk(car):
    is_in = False
    try:
        queryset = Propusk.objects.filter(car=car)
        if queryset.exists():
            print("На {} уже есть пропуск в БД".format(car.grz))
            is_in = Propusk.objects.get(car=car)
    except:
        is_in = False
    return is_in


def search_in_db_car(what):
    queryset = Car.objects.filter(grz=what)
    is_in = False
    if queryset.exists():
        print("Машина {} уже есть в БД".format(what))
        is_in = True
    return is_in


# Возвращает объект машины если она есть либо False
def obj_search_in_db_car(what):
    what = what.strip().upper()
    queryset = Car.objects.filter(grz=what)
    is_in = False
    if queryset.exists():
        print("Машина {} уже есть в БД".format(what))
        is_in = Car.objects.get(grz=what)
    return is_in


def obj_search_in_db_propusk(ser_type, ser):
    is_in = False
    try:
        print(ser)
        queryset = Propusk.objects.filter(serial_type=ser_type)
        queryset = queryset.filter(serial_num=ser)
        if queryset.exists():
            print("На {} уже есть пропуск в БД".format(ser))
            is_in = queryset
    except:
        is_in = False
    return is_in


def take_propusk_frome_allprovereno(file, request):
    print('take_propusk_frome_allprovereno')
    PATH_TO = "workstation/static/result/allprovereno.xlsx"
    propuska = []

    our = pyexcel.get_book_dict(file_name='workstation/static/fileupload/' + file.name)
    our_edit = []
    step = 0
    print('Взяли файл')
    print(len(our['Rabotaogon2']))
    for row in our['Rabotaogon2']:
        print("Скопировано {} строк из {}".format(step, len(our['Rabotaogon2'])))
        #print(row[0],row[1],row[2],row[3],row[4],row[5])
        if row[0] != '':
            if row[5] != '':
                days_to_end = row[5]
                days_to_end = str(days_to_end)
                temp = days_to_end.strip()
                temp = temp[0:3]
                days_to_end = temp.strip()
                if search_in_db_car(row[0]):
                    pass
                else:
                    date_from = datetime.strptime(row[1], "%d.%m.%Y").date().strftime("%Y-%m-%d")
                    date_to = datetime.strptime(row[2], "%d.%m.%Y").date().strftime("%Y-%m-%d")
                    db_car = Car(user_id=request.user, grz=row[0], is_our=True)
                    db_car.save()
                    # if row[3] == 'Активен':
                    #     status = 1
                    # if row[3] == 'Закончился':
                    #     status = 2
                    # if row[3] == 'Аннулирован':
                    #     status = 3

                    db_propusk = Propusk(car=db_car, date_from=date_from, date_to=date_to, status=row[3], days_to_end=days_to_end)
                    db_propusk.save()
                    propusk = {'grz': row[0], 'date_from': row[1], 'date_to': row[2], 'status': row[3], 'days_to_end': days_to_end, 'proverka': datetime.today().strftime("%Y-%m-%d")}
                    propuska.append(propusk)
            else:
                if search_in_db_car(row[0]):
                    pass
                else:
                    date_from = datetime.strptime(row[1], "%d.%m.%Y").date().strftime("%Y-%m-%d")
                    date_to = datetime.strptime(row[2], "%d.%m.%Y").date().strftime("%Y-%m-%d")
                    db_car = Car(user_id=request.user, grz=row[0], is_our=True)
                    db_car.save()
                    # if row[3] == 'Активен':
                    #     status = 1
                    # if row[3] == 'Закончился':
                    #     status = 2
                    # if row[3] == 'Аннулирован':
                    #     status = 3

                    db_propusk = Propusk(car=db_car, date_from=date_from, date_to=date_to, status=row[3])
                    db_propusk.save()
                    propusk = {'grz': row[0], 'date_from': row[1], 'date_to': row[2], 'status': row[3], 'proverka': datetime.today().strftime("%Y-%m-%d")}
                    propuska.append(propusk)
        step +=1
    print("Записанно в propuska {}".format(len(propuska)))
    wb = Workbook()
    ws = wb.active
    for prop in propuska:
        ws.append([prop['proverka'], prop['grz'], prop['date_from'], prop['date_to'], prop['status']])
    wb.save(PATH_TO)
    wb.close()


# Обновление БД, добавление новых машин(если их не было)
# если была, проверяем был ли такой пропуск, если нет и он свежее(либо по номеру пропуска,
# либо по дате действия), то записываем в БД
def add_annul_propusk_to_db(file, request):
    print('add_annul_propusk_to_db')
    our_annul_propuska = []
    annul = pyexcel.get_book_dict(file_name='workstation/static/fileupload/' + file.name)
    step = 0
    print('Взяли файл')
    print(len(annul['Sheet']))
    for row in annul['Sheet']:
        print("Проверенно {} строк из {}".format(step, len(annul['Sheet'])))
        if row[1] != '':
            car = obj_search_in_db_car(what=row[1])
            if car:
                # Если машина есть
                if car.is_our:
                    propusk = {'grz': row[1], 'date_from': row[2], 'date_to': row[3], 'status': row[4],
                               'proverka': datetime.today().strftime("%Y-%m-%d")}
                    print('Машина наша')
                    our_annul_propuska.append(propusk)

                    prop = Propusk.objects.filter(car=car)
                    if not prop:
                        print("Нет пропуска на " + car.grz)
                        date_from = datetime.strptime(row[2], "%d.%m.%Y").date().strftime("%Y-%m-%d")
                        date_to = datetime.strptime(row[3], "%d.%m.%Y").date().strftime("%Y-%m-%d")
                        propusk = Propusk(car=car, date_from=date_from, date_to=date_to, status=row[4])
                        propusk.save()
                else:
                    #Если машина есть но не наша
                    print('Машина не наша')
                    date_from = datetime.strptime(row[2], "%d.%m.%Y").date().strftime("%Y-%m-%d")
                    date_to = datetime.strptime(row[3], "%d.%m.%Y").date().strftime("%Y-%m-%d")
                    propusk = Propusk(car=car, date_from=date_from, date_to=date_to, status=row[4])
                    propusk.save()


            else:
                # Если машины нет
                car = Car(user_id=request.user, grz=row[1], is_our=False)
                car.save()
                date_from = datetime.strptime(row[2], "%d.%m.%Y").date().strftime("%Y-%m-%d")
                date_to = datetime.strptime(row[3], "%d.%m.%Y").date().strftime("%Y-%m-%d")
                propusk = Propusk(car=car, date_from=date_from, date_to=date_to, status=row[4])
                propusk.save()

        else:
            # Если пустая ячейка
            print('пустая ячейка')
        step += 1
        print("Записанно в propuska {}".format(len(our_annul_propuska)))
        save_to_file_annul(our_annul_propuska)
    return our_annul_propuska



def save_to_file_annul(propuska):
    PATH_TO = "workstation/static/result/annul.xlsx"
    try:
        wb = Workbook()
        ws = wb.active
        for prop in propuska:
            ws.append([prop['proverka'], prop['grz'], prop['date_from'], prop['date_to'], prop['status']])
        wb.save(PATH_TO)
        wb.close()
    except:
        print('Записать не удалось')


# проверка наличия файла
def can_i_take_file(path, name):
    file_name = path + name
    try:
        file = open(file_name)
    except IOError as e:
        print(u'не удалось открыть файл')
    else:
        with file:
            print(u'делаем что-то с файлом')


# отдельный модуль
# АвИнфоБот карта | связь с машиной(не наша?) и собственниками(новая таблица) и типом машины
# БД где хранятся все машины которые были проверены по АвИнфоБот
# добавление в базу данных клиентов с авИнфоБот, если есть тел номера
# если нет тел номера, тогда добавляем номер машины в БД как уже проверенную без номера тел.

# проверка есть ли в базе данных эти машины,


# Добавление пропусков в реестр с проверкой, наша машина или нет,
# если наша, тогда добавляем что пропуск наш, если не наша тогда создаем не нашу машину и доб пропуск
def add_propusk_to_reestr_ba(file, request):
    print("add_propusk_to_reestr_ba")
    # PATH_TO = "core/static/result/reestrBA.xlsx"
    propuska_new = []
    propuska_update = []

    our = pyexcel.get_book_dict(file_name='workstation/static/fileupload/' + file.name)
    step = 0
    print(len(our['БА']))
    for row in our['БА']:
        print("Скопировано {} строк из {}".format(step, len(our['БА'])))
        # print(row[0],row[1],row[2],row[3],row[4],row[5])
        if row[0] and row[1] != '':
            ser_type = row[0][0:2]
            ser_type = ser_type.strip()
            ser = row[0][2:10]
            ser = ser.strip()
            zone = row[4].strip()
            grz = row[1]
            grz = grz[0:9]
            grz = grz.strip()
            grz = grz.upper()
            if search_in_db_car(grz):
                car = Car.objects.get(grz=grz)
            else:
                car = Car(user_id=request.user, grz=grz, is_our=False)
                car.save()
            propusk = obj_search_by_car_in_db_propusk(car=car)
            today = date.today()
            # Проверка пропуска только по серии номера, нужно добавить проверку пропуска по госномеру
            if not search_in_db_propusk(ser_type, ser):
                # Если пропуска нет в БД по серии и номеру, то проверяем есть ли по госзнаку пропуск на машину
                if propusk:
                    # если по госзнаку есть пропуск, то проверяем даты пропусков, если они совподают, тогда
                    # перезаписываем пропуск и добавляем в него серию и номер, где действует
                    try:
                        date_from = str(row[2])[:10]
                        date_to = str(row[3])[:10]
                        date_from = datetime.strptime(date_from, "%Y-%m-%d").date().strftime("%Y-%m-%d")
                        date_to = datetime.strptime(date_to, "%Y-%m-%d").date().strftime("%Y-%m-%d")
                        days_to_end = row[3] - datetime.now()

                    except:
                        try:
                            date_from = str(row[2])[:10]
                            date_to = str(row[3])[:10]
                            date_to = datetime.strptime(date_to, "%d.%m.%Y").date()
                            today = date.today()
                            # today = today.strftime("%Y-%m-%d")
                            # print(today)
                            days_to_end = date_to - today
                            date_to = str(row[3])[:10]
                            date_from = datetime.strptime(date_from, "%d.%m.%Y").date().strftime("%Y-%m-%d")
                            date_to = datetime.strptime(date_to, "%d.%m.%Y").date().strftime("%Y-%m-%d")

                        except:
                            print('на {} возникла проблема с форматом дат'.format(grz))

                    propusk_date_from = propusk.date_from
                    propusk_date_to = propusk.date_to
                    if propusk_date_from == date_from and propusk_date_to == date_to:
                        propusk.serial_type = ser_type
                        propusk.serial_num = ser
                        propusk.zone_type = zone
                        propusk.days_to_end = days_to_end
                        propusk.save()

                        propuska_update.append(car.grz)
                    else:
                        #Если по госномеру есть пропуск, но по датам есть расхождения, значит создаем новый пропуск
                        try:
                            date_from = str(row[2])[:10]
                            date_to = str(row[3])[:10]
                            date_from = datetime.strptime(date_from, "%Y-%m-%d").date().strftime("%Y-%m-%d")
                            date_to = datetime.strptime(date_to, "%Y-%m-%d").date().strftime("%Y-%m-%d")
                            days_to_end = row[3] - datetime.now()
                            if row[5] != '':
                                status = row[5].strip()
                                if status == 'Выдан' and row[3] > datetime.now():
                                    status = 'Активен'
                                else:
                                    status = 'Закончился'

                        except:
                            try:
                                date_from = str(row[2])[:10]
                                date_to = str(row[3])[:10]
                                date_to = datetime.strptime(date_to, "%d.%m.%Y").date()
                                # today = today.strftime("%Y-%m-%d")
                                # print(today)
                                days_to_end = date_to - today
                                if row[5] != '':
                                    status = row[5].strip()
                                    if status == 'Выдан' and date_to > today:
                                        status = 'Активен'
                                    else:
                                        status = 'Закончился'
                                date_to = str(row[3])[:10]
                                date_from = datetime.strptime(date_from, "%d.%m.%Y").date().strftime("%Y-%m-%d")
                                date_to = datetime.strptime(date_to, "%d.%m.%Y").date().strftime("%Y-%m-%d")

                            except:
                                print('на {} возникла проблема с форматом дат'.format(grz))

                        propusk = Propusk(car=car, zone_type=zone, serial_type=ser_type, serial_num=ser,
                                          date_from=date_from, date_to=date_to, status=status)
                        propusk.save()
                        propuska_new.append(car.grz)
                else:
                    # Если по госзнаку нет, создаем новый
                    try:
                        date_from = str(row[2])[:10]
                        date_to = str(row[3])[:10]
                        date_from = datetime.strptime(date_from, "%Y-%m-%d").date().strftime("%Y-%m-%d")
                        date_to = datetime.strptime(date_to, "%Y-%m-%d").date().strftime("%Y-%m-%d")
                        days_to_end = row[3] - datetime.now()
                        if row[5] != '':
                            status = row[5].strip()
                            if status == 'Выдан' and row[3] > datetime.now():
                                status = 'Активен'
                            else:
                                status = 'Закончился'

                    except:
                        try:
                            date_from = str(row[2])[:10]
                            date_to = str(row[3])[:10]
                            date_to = datetime.strptime(date_to, "%d.%m.%Y").date()
                            # today = today.strftime("%Y-%m-%d")
                            # print(today)
                            days_to_end = date_to - today
                            if row[5] != '':
                                status = row[5].strip()
                                if status == 'Выдан' and date_to > today:
                                    status = 'Активен'
                                else:
                                    status = 'Закончился'
                            date_to = str(row[3])[:10]
                            date_from = datetime.strptime(date_from, "%d.%m.%Y").date().strftime("%Y-%m-%d")
                            date_to = datetime.strptime(date_to, "%d.%m.%Y").date().strftime("%Y-%m-%d")

                        except:
                            print('на {} возникла проблема с форматом дат'.format(grz))
                    propusk = Propusk(car=car, zone_type=zone, serial_type=ser_type, serial_num=ser, date_from=date_from, date_to=date_to, status=status)
                    propusk.save()
                    propuska_new.append(car.grz)
            else:
                # Если пропуск есть по серии и номеру то обновляем статус и дней до
                try:
                    date_from = str(row[2])[:10]
                    date_to = str(row[3])[:10]
                    date_from = datetime.strptime(date_from, "%Y-%m-%d").date().strftime("%Y-%m-%d")
                    date_to = datetime.strptime(date_to, "%Y-%m-%d").date().strftime("%Y-%m-%d")
                    days_to_end = row[3] - datetime.now()
                    if row[5] != '':
                        status = row[5].strip()
                        if status == 'Выдан' and row[3] > datetime.now():
                            status = 'Активен'
                        else:
                            status = 'Закончился'

                except:
                    try:
                        date_from = str(row[2])[:10]
                        date_to = str(row[3])[:10]
                        date_to = datetime.strptime(date_to, "%d.%m.%Y").date()
                        # today = today.strftime("%Y-%m-%d")
                        # print(today)
                        days_to_end = date_to - today
                        if row[5] != '':
                            status = row[5].strip()
                            if status == 'Выдан' and date_to > today:
                                status = 'Активен'
                            else:
                                status = 'Закончился'
                        date_to = str(row[3])[:10]
                        date_from = datetime.strptime(date_from, "%d.%m.%Y").date().strftime("%Y-%m-%d")
                        date_to = datetime.strptime(date_to, "%d.%m.%Y").date().strftime("%Y-%m-%d")

                    except:
                        print('на {} возникла проблема с форматом дат'.format(grz))
                propusk.status = status
                propusk.days_to_end = days_to_end
                propusk.save()

                propuska_update.append(car.grz)
            step += 1
        else:
            print('Пустая ячека')


    if len(propuska_update) > 0:
        print("Обновленно старых {}".format(len(propuska_update)))
    else:
        print('Ничего не обновляли')

    if len(propuska_new) > 0:
        print("Записанно новых {}".format(len(propuska_new)))
    else:
        print('Ничего нового не добавили')



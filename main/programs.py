import pyexcel
from datetime import timedelta
from .models import Car #Propusk,
#from anticaptchaofficial.recaptchav2proxyless import *
#from openpyxl import Workbook
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import datetime as dt
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# #from anticaptchaofficial.imagecaptcha import *
# from PIL import Image


def handle_uploaded_file(request, file, program):
    if program == 'add_file_annul':
        print('handle_uploaded_file add_file_annul')
        with open('workstation/static/fileupload/' + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        print('file saved')
    if program == 'add_file_our_cars':
        print('handle_uploaded_file add_file_our_cars')
        with open('workstation/static/fileupload/' + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        print('file saved')
       # take_propusk_frome_allprovereno(file=file, request=request)

#
# def search_in_db_propusk(ser_type, ser):
#     is_in = False
#     try:
#         print(ser)
#         queryset = Propusk.objects.filter(serial_type=ser_type)
#         queryset = queryset.filter(serial_num=ser)
#         if queryset.exists():
#             print("На {} уже есть пропуск в БД".format(ser))
#             is_in = True
#     except:
#         is_in = False
#     return is_in
#
#
# def take_propusk_frome_allprovereno(file, request):
#     PATH_TO = "main/static/result/step2.xlsx"
#     propuska = []
#
#     our = pyexcel.get_book_dict(file_name='main/static/fileupload/' + file.name)
#     our_edit = []
#     step = 0
#     print(len(our['Rabotaogon2']))
#     for row in our['Rabotaogon2']:
#         print("Скопировано {} строк из {}".format(step, len(our['Rabotaogon2'])))
#         #print(row[0],row[1],row[2],row[3],row[4],row[5])
#         if row[0] != '':
#             if row[5] != '':
#                 days_to_end = row[5]
#                 days_to_end = str(days_to_end)
#                 temp = days_to_end.strip()
#                 temp = temp[0:3]
#                 days_to_end = temp.strip()
#                 if search_in_db_car(row[0]):
#                     pass
#                 else:
#                     date_from = datetime.strptime(row[1], "%d.%m.%Y").date().strftime("%Y-%m-%d")
#                     date_to = datetime.strptime(row[2], "%d.%m.%Y").date().strftime("%Y-%m-%d")
#                     db_car = Car(user_id=request.user,grz=row[0])
#                     db_car.save()
#                     db_propusk = Propusk(car=db_car, date_from=date_from, date_to=date_to, status=row[3], days_to_end=days_to_end)
#                     db_propusk.save()
#                     propusk = {'grz': row[0], 'date_from': row[1], 'date_to': row[2], 'status': row[3], 'days_to_end': days_to_end, 'proverka': datetime.today().strftime("%Y-%m-%d")}
#                     propuska.append(propusk)
#             else:
#                 if search_in_db_car(row[0]):
#                     pass
#                 else:
#                     date_from = datetime.strptime(row[1], "%d.%m.%Y").date().strftime("%Y-%m-%d")
#                     date_to = datetime.strptime(row[2], "%d.%m.%Y").date().strftime("%Y-%m-%d")
#                     db_car = Car(grz=row[0])
#                     db_car.save()
#                     db_propusk = Propusk(car=db_car, date_from=date_from, date_to=date_to, status=row[3])
#                     db_propusk.save()
#                     propusk = {'grz': row[0], 'date_from': row[1], 'date_to': row[2], 'status': row[3], 'proverka' : datetime.today().strftime("%Y-%m-%d")}
#                     propuska.append(propusk)
#         step +=1
#     print("Записанно в propuska {}".format(len(propuska)))
#     wb = Workbook()
#     ws = wb.active
#     for prop in propuska:
#         ws.append([prop['proverka'],prop['grz'],prop['date_from'],prop['date_to'],prop['status']])
#     wb.save(PATH_TO)
#     wb.close()
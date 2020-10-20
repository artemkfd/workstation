from datetime import timedelta

from django.shortcuts import render, get_object_or_404, redirect
from .programs import handle_uploaded_file
from .forms import uploadFileForm, doubles
from .models import Car
import time

def main_view(request):
    return render(request, 'main/main.html')


def settings_view(request):
    return render(request, 'main/settings.html')


def add_file_our_cars_view(request):
    start_time = time.monotonic()
    form = uploadFileForm()
    if request.method == "POST":
        print(request.POST)
        print(request.POST['textarea_array'])
        print(len(request.POST['textarea_array']))
        if request.POST.get('textarea_array'):
            print('textarea_array exists')
        else:
            print('no textarea_array')

        form = uploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print('file exists')
            print("Форма валидна")
            program = 'add_file_our_cars'
            handle_uploaded_file(request=request, file=request.FILES['file'], program=program)
            print("Файл добавлен успешно")
            end_time = time.monotonic()
            timefromstart = timedelta(seconds=end_time - start_time)
            print("Времени на загрузку заняло {}".format(timefromstart))
            return render(request, 'main/main.html',
                          {'status': "Файл добавлен успешно", 'timefromstart': timefromstart})
        else:
            print('no file')
            form = uploadFileForm()

        if request.POST.get('type'):
            print('type exists')
        else:
            print('no type')

    return render(request, 'main/add_file_annul.html', {'form': form})


def add_file_annul_view(request):
    start_time = time.monotonic()
    form = uploadFileForm()
    if request.method == "POST":
        print(request.POST)
        print(request.POST['textarea_array'])
        print(len(request.POST['textarea_array']))
        if request.POST.get('textarea_array'):
            print('textarea_array exists')
        else:
            print('no textarea_array')

        form = uploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print('file exists')
            print("Форма валидна")
            program = 'add_file_annul'
            handle_uploaded_file(request=request, file=request.FILES['file'], program=program)
            print("Файл добавлен успешно")
            end_time = time.monotonic()
            timefromstart = timedelta(seconds=end_time - start_time)
            print("Времени на загрузку заняло {}".format(timefromstart))
            return render(request, 'main/main.html',
                          {'status': "Файл добавлен успешно", 'timefromstart': timefromstart})
        else:
            print('no file')
            form = uploadFileForm()

        if request.POST.get('type'):
            print('type exists')
        else:
            print('no type')

    return render(request, 'main/add_file_annul.html', {'form': form})


def find_our_cars_view(request):
    form = doubles()
    if request.method == "POST":
        # form = doubles(request.POST)
        print(request.POST)
        if 'text' in request.POST:
            print(request.POST['text'][0:9])
            print(len(request.POST['text']))
            numbers = request.POST['text'].split()
            print(numbers)
            print(len(numbers))
            if len(numbers[0]) <= 9:
                print('valid data')
                temp = Car.objects.all()
                print(len(temp))
                cars = []
                for n in numbers:
                    if len(n) > 6:
                        temp = Car.objects.filter(grz=n)
                        if temp.exists():
                            print('{} такой номер есть'.format(n))

                            # c = Car(grz=n)
                            # c.save()
                            car = {'grz': n, 'status': 'такой номер есть'}
                        else:
                            print('{} нет номера'.format(n))
                            car = {'grz': n, 'status': 'нет номера'}
                            c = Car(user_id=request.user, grz=n)
                            c.save()
                        cars.append(car)
                    else:
                        print('valid 2 error')

            # wb = Workbook()
            # ws = wb.active
            # if len(cars) > 0:
            # for car in cars:
            # print(prop)
            # ws.append([car['grz'], car['status']])
            # wb.save('Checkcars.xlsx')
            # wb.close()
            # print('Записанно пропусков :', len(cars))
            # else:
            # print('Нет пропусков')
            else:
                print('not valid data')

            # form = doubles(cars)
            return render(request, 'main/find_our_cars_result.html', {'cars': cars})

    return render(request, 'main/find_our_cars.html')
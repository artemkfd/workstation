
from main.models import Car, Propusk
from django.shortcuts import render
from django.db.models import Q


def search_view(request):
    query = None
    results = []
    propusks = []
    if request.method == 'GET':
        print("Get method")
        print(request.GET)
        print(request.GET['search_value'])
        query = request.GET.get('search_value')

        results = Car.objects.filter(Q(grz__icontains=query))
        print(results[0].is_our)
        print(results[0].grz)
        print(results[0].user_id)
        print(results[0].create_date)
        prop = None
        for result in results:
            try:
                prop = Propusk.objects.filter(car=result)
            except:
                print('no propusk')
            if prop:
                propusks.append(prop)
        print(propusks)
        if len(propusks) > 0:
            print(propusks[0])
            print(propusks[0][0])

    return render(request,'search/search.html', {'query': query, 'results': results, 'propusks': propusks})


def car_info(request, car_id):
    car = Car.objects.get(id=car_id)
    propusk = None
    try:
        propusk = Propusk.objects.get(car=car)
    except:
        print('нет пропусков')
    return render(request,'main/car_info.html', {'car':  car, 'propusk':propusk})
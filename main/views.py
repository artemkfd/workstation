from django.shortcuts import render, get_object_or_404, redirect


def mainView(request):
    return render(request, 'main/main.html')


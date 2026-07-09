from django.shortcuts import render


def contact(request):
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')
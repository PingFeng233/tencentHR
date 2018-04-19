from django.shortcuts import render


# Create your views here.

def info(request):
    return render(request, 'about/info.html')


def branch(request):
    return render(request, 'about/areas.html')


def business(request):
    return render(request, 'about/businessSystem.html')


def culture(request):
    return render(request, 'about/culture.html')

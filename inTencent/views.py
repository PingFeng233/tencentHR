from django.shortcuts import render


# Create your views here.

def work(request):
    return render(request, 'inTencent/work.html')


def live(request):
    return render(request, 'inTencent/live.html')


def training(request):
    return render(request, 'inTencent/training.html')


def welfare(request):
    return render(request, 'inTencent/welfare.html')

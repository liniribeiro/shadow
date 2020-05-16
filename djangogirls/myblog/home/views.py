from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


def other(request):
    context = {
        'k1': 'Welcome to the Second page',
    }
    return render(request, 'others.html', context)

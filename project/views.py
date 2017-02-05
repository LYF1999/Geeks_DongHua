from django.shortcuts import render


def open_source(request):
    return render(request, 'index.html')


def software(request):
    return render(request, 'index.html')

# Create your views here.

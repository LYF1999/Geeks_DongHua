from django.shortcuts import render


def fix(request):
    return render(request, 'index.html')


def fix_command(request):
    return render(request, 'index.html')

# Create your views here.

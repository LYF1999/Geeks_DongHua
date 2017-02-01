#  coding=utf-8
from django.shortcuts import render


def login(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'index.html')

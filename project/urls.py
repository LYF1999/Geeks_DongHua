#  coding=utf-8
from django.conf.urls import url
from project.views import *

urlpatterns = [
    url(r'^open_source/', open_source),
    url(r'^software/', software)
]

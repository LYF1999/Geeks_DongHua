from django.conf.urls import url
from myuser.views import *

urlpatterns = [
    url(r'login/$', login),
    url(r'register/$', register),
    url(r'profile', profile)
]
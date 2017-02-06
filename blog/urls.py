#  coding=utf-8
from __future__ import unicode_literals

from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url('^edit', edit)
]

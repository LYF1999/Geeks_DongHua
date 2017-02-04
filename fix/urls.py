from django.conf.urls import url

from fix.views import *
urlpatterns = [
    url('^$', fix),
    url('^command/$', fix_command)
]

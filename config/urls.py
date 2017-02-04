"""Geeks_DongHua URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import render

from config import settings
from config.router import router
from home import index
from fix.views import fix

urlpatterns = [
    url(r'^admin/+', admin.site.urls),

    url(r'^api/', include(router.urls, namespace='rest_framework')),

    url(r'^$', index, name='index'),
    url(r'^myadmin/', index),
    url(r'fix/', include('fix.urls')),
    url(r'user/', include('myuser.urls', namespace='myuser')),
    url(r'project/', include('project.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


def handler404(request):
    return render(request, 'index.html', locals())

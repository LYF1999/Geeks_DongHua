#  coding=utf-8

from django.conf import settings
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import list_route

from blog.api.serializers import BlogSerializer
from blog.api.forms import ImgUploadForm
from blog.models import Blog

import os


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, **kwargs):
        return Blog.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        form = BlogSerializer(data=request.data)
        form.is_valid(raise_exception=True)
        Blog.objects.create(
            title=form.data['title'],
            content=form.data['content'],
            user=request.user,
            active=form.data['active']
        )
        return Response({
            u'message': u'操作成功',
            u'data': form.data,
        })

    @list_route(methods=['POST'], permission_classes=[permissions.IsAuthenticated], serializer_class=ImgUploadForm)
    def upload_img(self, request):
        img_folder_path = os.path.join('media', 'img')
        form = ImgUploadForm(data=request.data)
        form.is_valid(raise_exception=True)
        token = request.user.username
        img = request.FILES['wangEditorH5File']
        img_path = os.path.join(img_folder_path, token + '-' + img.name)
        with open(img_path, 'wb+') as f:
            for chunk in img.chunks():
                f.write(chunk)
        return HttpResponse(u'http://%s/' % settings.DOMAIN + img_path, content_type='text/x-json')
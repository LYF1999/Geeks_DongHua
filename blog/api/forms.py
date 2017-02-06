#  coding=utf-8
from rest_framework import serializers


class ImgUploadForm(serializers.Serializer):
    wangEditorH5File = serializers.FileField()

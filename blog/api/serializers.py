#  coding=utf-8
from __future__ import unicode_literals
from rest_framework import serializers

from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['user']

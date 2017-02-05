#  coding=utf-8
from __future__ import unicode_literals

from rest_framework import serializers

from project.models import OpenSourceProject, SoftWare


class OpenSourceProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenSourceProject
        fields = '__all__'


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftWare
        fields = '__all__'

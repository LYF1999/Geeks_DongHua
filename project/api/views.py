#  coding=utf-8
from __future__ import unicode_literals

from rest_framework import viewsets, permissions

from project.api.serializers import OpenSourceProjectSerializer, SoftwareSerializer
from project.models import OpenSourceProject, SoftWare


class OpenSourceProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OpenSourceProjectSerializer
    permission_classes = [permissions.AllowAny]
    queryset = OpenSourceProject.objects.all()


class SoftwareViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SoftwareSerializer
    permission_classes = [permissions.AllowAny]
    queryset = SoftWare.objects.all()

#  coding=utf-8
from __future__ import unicode_literals

from rest_framework import viewsets, permissions

from project.api.serializers import OpenSourceProjectSerializer, SoftwareSerializer
from project.models import OpenSourceProject, Tool


class OpenSourceProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OpenSourceProjectSerializer
    permission_classes = [permissions.AllowAny]
    queryset = OpenSourceProject.objects.all()


class ToolViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SoftwareSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Tool.objects.all()

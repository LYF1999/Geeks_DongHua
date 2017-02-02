#  coding=utf-8
from __future__ import unicode_literals

from rest_framework import viewsets, permissions

from project.api.serializers import OpenSourceProjectSerializer
from project.models import OpenSourceProject


class OpenSourceProjectViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OpenSourceProjectSerializer
    permission_classes = [permissions.AllowAny]
    queryset = OpenSourceProject.objects.all()

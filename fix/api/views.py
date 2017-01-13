# coding=utf-8
from __future__ import unicode_literals
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

from fix.api.serializers import FixSerializer
from fix.api.forms import AppointmentForm
from fix.models import Fix


class FixViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Fix.objects.all()
    serializer_class = FixSerializer

    @list_route(methods=['POST'], permission_classes=[permissions.AllowAny], serializer_class=AppointmentForm)
    def appointment(self, request):
        form = AppointmentForm(data=request.data)
        form.is_valid(raise_exception=True)
        form.save()
        return Response({'result': True, 'data': form.data})

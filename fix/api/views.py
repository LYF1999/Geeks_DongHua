# coding=utf-8
from __future__ import unicode_literals
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import list_route

from myglobal.models import FixStatus
from fix.api.serializers import FixSerializer, FaultSerializer
from fix.api.forms import AppointmentForm
from fix.api.throttles import FixRateThrottle
from fix.models import Fix, Fault


class FixViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Fix.objects.all()
    serializer_class = FixSerializer

    @list_route(methods=['POST'], throttle_classes=[FixRateThrottle], permission_classes=[permissions.AllowAny],
                serializer_class=AppointmentForm)
    def appointment(self, request):
        form = AppointmentForm(data=request.data)
        form.is_valid(raise_exception=True)

        fix_status = FixStatus.get_fix_status()

        if not fix_status.status:
            return Response({'detail': fix_status.message}, status=status.HTTP_406_NOT_ACCEPTABLE)

        form.save()
        return Response({'message': '成功预约', 'data': form.data}, status=200)

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def get_faults(self, request):
        serializer = FaultSerializer(Fault.objects.all(), many=True)
        return Response(serializer.data, status=200)

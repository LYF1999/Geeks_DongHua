# coding=utf-8
from __future__ import unicode_literals
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

from myglobal.models import FixStatus
from fix.api.serializers import FixSerializer, FaultSerializer
from fix.api.permissions import FixPermission
from fix.api.forms import AppointmentForm
from fix.api.throttles import FixRateThrottle
from fix.models import Fix, Fault


class FixViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions, permissions.IsAdminUser)
    queryset = Fix.objects.all()
    serializer_class = FixSerializer

    @list_route(methods=['POST'], throttle_classes=[FixRateThrottle, ], permission_classes=[permissions.AllowAny],
                serializer_class=AppointmentForm)
    def appointment(self, request):
        form = AppointmentForm(data=request.data)
        form.is_valid(raise_exception=True)

        fix_status = FixStatus.get_fix_status()

        if not fix_status.status:
            return Response({'message': fix_status.message}, status=status.HTTP_406_NOT_ACCEPTABLE)

        form.save()
        return Response({'message': '成功预约', 'data': form.data}, status=200)

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def get_faults(self, request):
        serializer = FaultSerializer(Fault.objects.all(), many=True)
        return Response(serializer.data, status=200)

    @list_route(methods=['GET'], permission_classes=[FixPermission])
    def get_not_receive(self, request):
        serializer = FixSerializer(Fix.objects.filter(fixer=None, is_fix=False), many=True)
        return Response(serializer.data)

    @list_route(methods=['GET'], permission_classes=[FixPermission])
    def get_my_order(self, request):
        return Response(FixSerializer(Fix.objects.filter(fixer=request.user), many=True).data, status=200)

    @detail_route(methods=['POST'], permission_classes=[FixPermission])
    def receive(self, request, pk):
        fix_order = self.get_object()
        if fix_order.fixer:
            return Response({
                'message': '订单已被接受'
            }, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'receive' not in request.data:
            return Response({'message': '错误操作'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if request.data['receive']:
            fix_order.fixer = request.user
            fix_order.save()

        return Response({
            'data': FixSerializer(fix_order).data,
            'message': '接单成功'
        }, status=200)

    @detail_route(methods=['POST'], permission_classes=[permissions.IsAdminUser, permissions.DjangoModelPermissions])
    def finish(self, request, pk):
        fix_order = self.get_object()

        if fix_order.fixer != request.user:
            return Response({'message': '你不是该订单的维修者'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'finish' not in request.data:
            return Response({'message': '错误操作'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'model' not in request.data:
            return Response({'message': '机型没有填写'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        if request.data['finish']:
            fix_order.is_fix = True
            fix_order.model = request.data['model']
            fix_order.save()

        return Response({
            'data': FixSerializer(fix_order).data,
            'message': '恭喜您又完成了一次义修'
        }, status=200)

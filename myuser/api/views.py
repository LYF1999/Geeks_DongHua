# coding=utf-8
from __future__ import unicode_literals
from myuser.api.serializers import AccountSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from rest_framework import viewsets, permissions
from rest_framework.decorators import list_route
from rest_framework.response import Response

from myuser.api.forms import LoginForm, RegisterForm
from myuser.models import User


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAdminUser, permissions.DjangoObjectPermissions]
    queryset = User.objects.all()

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def get_profile(self, request):
        user = request.user
        if not user.is_authenticated():
            return Response({
                'auth': False
            })
        serializer = AccountSerializer(user)
        return Response(serializer.data)

    @list_route(methods=['POST'], serializer_class=LoginForm, permission_classes=[permissions.AllowAny])
    def login(self, request):
        form = LoginForm(data=request.data)
        form.is_valid(raise_exception=True)
        user = authenticate(username=form.data['username'], password=form.data['password'])
        if user and user.is_authenticated:
            login(request, user)
            return Response({'result': True})
        return Response({'result': False, 'detail': '账户或者密码错误'})

    @list_route(methods=['POST'], serializer_class=RegisterForm, permission_classes=[permissions.AllowAny])
    def register(self, request):
        form = RegisterForm(data=request.data)
        form.is_valid(raise_exception=True)
        user = User.objects.create_user(
            username=form.data['username'],
            password=form.data['password'],
            tel=form.data['tel'],
            full_name=form.data['name']
        )
        login(request, user)
        return Response({'result': True, 'detail': form.data})

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def logout(self, request):
        logout(request)
        return Response({'result': True})

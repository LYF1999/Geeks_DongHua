# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

from rest_framework import viewsets, permissions, status
from rest_framework.decorators import list_route
from rest_framework.response import Response

from myuser.api.serializers import AccountSerializer
from myuser.api.forms import LoginForm, RegisterForm, ModifyProfileForm
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
        data = AccountSerializer(user).data
        data['auth'] = True
        return Response(data)

    @list_route(methods=['PATCH'], permission_classes=[permissions.AllowAny], serializer_class=ModifyProfileForm)
    def modify_profile(self, request):
        form = ModifyProfileForm(request.data)
        form.is_valid(raise_exception=True)
        user = request.user
        user.name = form.data['name']
        user.qq = form.qq['qq']
        user.save()
        return Response({'message': '修改成功', 'data': form.data}, status=200)

    @list_route(methods=['POST'], serializer_class=LoginForm, permission_classes=[permissions.AllowAny])
    def login(self, request):
        form = LoginForm(data=request.data)
        form.is_valid(raise_exception=True)
        user = authenticate(username=form.data['username'], password=form.data['password'])
        if user and user.is_authenticated:
            login(request, user)
            redirect_url = '/'
            return Response({'message': '您已成功登陆'}, status=status.HTTP_200_OK)
        return Response({'message': '账户或者密码错误'}, status=status.HTTP_401_UNAUTHORIZED)

    @list_route(methods=['POST'], serializer_class=RegisterForm, permission_classes=[permissions.AllowAny])
    def register(self, request):
        form = RegisterForm(data=request.data)
        form.is_valid(raise_exception=True)
        user = User.objects.create_user(
            full_name=form.data['name'],
            username=form.data['username'],
            password=form.data['password'],
            tel=form.data['tel'],
        )
        login(request, user)
        return Response({'message': '注册成功'}, status=200)

    @list_route(methods=['GET'], permission_classes=[permissions.AllowAny])
    def logout(self, request):
        logout(request)
        return Response({'message': '您已注销'}, status=200)

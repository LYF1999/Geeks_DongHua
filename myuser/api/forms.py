# coding=utf-8
from rest_framework import serializers

from myuser.models import User


class LoginForm(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterForm(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    repeat_password = serializers.CharField()
    tel = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(u"该用户名已经注册")
        return username

    def validate_password(self, password):
        if self.initial_data['repeat_password'] != password:
            raise serializers.ValidationError(u"两次密码输入不一致")
        return password

    def validate_tel(self, tel):
        if User.objects.filter(tel=tel).exists():
            raise serializers.ValidationError(u"该电话号码已经注册")
        return tel

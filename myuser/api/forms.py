# coding=utf-8
from rest_framework import serializers

from myuser.models import User

from util import is_valid_tel

import re


class LoginForm(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterForm(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    tel = serializers.CharField()

    def validate_username(self, username):
        if re.search(r'admin|root', username, re.I):
            raise serializers.ValidationError(u'用户名含有非法词汇')
        if not re.match(r'\w+', username):
            raise serializers.ValidationError(u'用户名只允许字母和数字')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(u"该用户名已经注册")
        return username

    def validate_tel(self, tel):
        if not is_valid_tel(tel):
            raise serializers.ValidationError(u'电话号码格式错误')
        if User.objects.filter(tel=tel).exists():
            raise serializers.ValidationError(u"该电话号码已经注册")
        return tel

from rest_framework import serializers
from myuser.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'password', 'last_login', 'register_time', 'groups', 'user_permissions')

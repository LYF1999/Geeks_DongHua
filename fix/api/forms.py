# coding=utf-8
from rest_framework import serializers
from fix.models import Fix

from util import is_valid_tel


class AppointmentForm(serializers.ModelSerializer):
    class Meta:
        model = Fix
        exclude = ('appointment_time', 'fixer', 'fix_time', 'is_fix')

    def validate_tel(self, tel):
        if not is_valid_tel(tel):
            raise serializers.ValidationError(u'电话号码格式错误')
        return tel

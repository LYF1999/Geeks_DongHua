# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from fix.constants import FAULT_CHOICE
from myuser.models import User


class Fix(models.Model):
    #  预约信息
    name = models.CharField(u'姓名', max_length=255)
    dorm_number = models.IntegerField(u'楼号')
    tel = models.CharField(u'电话', max_length=255)
    fault = models.IntegerField(choices=FAULT_CHOICE)
    mark = models.TextField(u'备注', blank=True, default='')
    appointment_time = models.DateTimeField(u'预约时间', default=timezone.now)

    # 维修信息
    fixer = models.OneToOneField(User, verbose_name=u'修理员', null=True, default=None)
    fix_time = models.DateTimeField(u'修理时间', null=True, default=None)

# Create your models here.

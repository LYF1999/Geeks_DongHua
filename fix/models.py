# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from myuser.models import User
from myuser.constants import Sex_Choice
from util import format_time


class Fault(models.Model):
    name = models.CharField('故障', max_length=255)
    order = models.IntegerField('排序', null=True, blank=True)

    class Meta:
        verbose_name = '故障列表'
        verbose_name_plural = verbose_name
        ordering = ('order',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % self.name


class Fix(models.Model):
    #  预约信息
    name = models.CharField('姓名', max_length=255)
    dorm_number = models.IntegerField(u'楼号')
    tel = models.CharField('电话', max_length=255)
    fault = models.ForeignKey(Fault, verbose_name='故障')
    mark = models.TextField('备注', blank=True, default='')
    appointment_time = models.DateTimeField(u'预约时间', default=timezone.now)

    # 维修信息
    model = models.CharField(max_length=255, null=True, blank=True)
    fixer = models.ForeignKey(User, verbose_name='修理员', null=True, default=None)
    fix_time = models.DateTimeField('修理时间', blank=True, null=True)
    is_fix = models.BooleanField('是否维修', default=False)

    class Meta:
        verbose_name = '预约名单'
        verbose_name_plural = verbose_name
        ordering = ('is_fix', '-appointment_time')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % self.name

    def get_fault(self):
        return self.fault.name

    def get_appointment_time(self):
        return format_time(self.appointment_time)

    def get_fix_time(self):
        return format_time(self.fix_time)


class Recruit(models.Model):
    name = models.CharField('姓名', max_length=255)
    sex = models.IntegerField('性别', choices=Sex_Choice)
    tel = models.CharField('电话', max_length=255)
    major = models.CharField('专业', max_length=255)
    desc = models.TextField()
    reason = models.TextField(blank=True, null=True)

# Create your models here.

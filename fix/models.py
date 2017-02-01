# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from myuser.models import User


class Fault(models.Model):
    name = models.CharField('故障', max_length=255)

    class Meta:
        verbose_name = '故障列表'
        verbose_name_plural = verbose_name

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
    fixer = models.OneToOneField(User, verbose_name='修理员', null=True, default=None)
    fix_time = models.DateTimeField('修理时间', null=True, default=None)
    is_fix = models.BooleanField('是否维修', default=False)

    class Meta:
        verbose_name = '预约名单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def __unicode__(self):
        return '%s' % self.name

# Create your models here.

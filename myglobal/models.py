# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class FixStatus(models.Model):
    message = models.CharField('留言', max_length=255)
    status = models.BooleanField('状态', default=False)
    time = models.DateTimeField('添加日期', auto_now_add=True, editable=True)

    class Meta:
        verbose_name = '维修状态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message

    def __unicode__(self):
        return '%s' % self.message

    @classmethod
    def get_fix_status(cls):
        if not cls.objects.first():
            cls.objects.create(message='义修还未开启呢', status=False)

        fix_status = cls.objects.first()
        return fix_status

# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from myuser.models import User


class Blog(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')

    title = models.CharField('标题', max_length=255)
    content = models.TextField('内容')

    active = models.BooleanField('发表状态')
    publish_time = models.DateTimeField('发表时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

# Create your models here.

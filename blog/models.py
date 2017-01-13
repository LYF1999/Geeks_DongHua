# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from myuser.models import User


class Blog(models.Model):
    user = models.OneToOneField(User, verbose_name='用户')

    title = models.CharField('标题')
    content = models.TextField('内容')

    active = models.BooleanField('发表状态')
    publish_time = models.DateTimeField('发表时间')
    update_time = models.DateTimeField('修改时间')

# Create your models here.

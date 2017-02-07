# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class OpenSourceProject(models.Model):
    name = models.CharField('名称', max_length=255)
    url = models.URLField('地址', blank=True, default='')
    message = models.TextField(blank=True, default='')
    order = models.IntegerField('排序', null=True, blank=True)

    class Meta:
        verbose_name = '开源项目'
        verbose_name_plural = '开源项目'
        ordering = ('order',)


class Tool(models.Model):
    name = models.CharField('名称', max_length=255)
    url = models.URLField('链接', blank=True, default='')
    message = models.TextField(blank=True, default='')
    order = models.IntegerField('排序', null=True, blank=True)

    class Meta:
        verbose_name = '常用工具'
        verbose_name_plural = '常用工具'
        ordering = ('order', )

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='\u90ae\u7bb1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='qq',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='QQ\u53f7'),
        ),
    ]

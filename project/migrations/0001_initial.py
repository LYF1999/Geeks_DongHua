# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OpenSourceProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u540d\u79f0')),
                ('url', models.URLField(blank=True, default='', verbose_name='\u5730\u5740')),
            ],
            options={
                'verbose_name': '\u5f00\u6e90\u9879\u76ee',
                'verbose_name_plural': '\u5f00\u6e90\u9879\u76ee',
            },
        ),
    ]

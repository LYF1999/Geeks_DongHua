# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fix', '0003_fix_model'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fault',
            options={'ordering': ('-order',), 'verbose_name': '\u6545\u969c\u5217\u8868', 'verbose_name_plural': '\u6545\u969c\u5217\u8868'},
        ),
        migrations.AddField(
            model_name='fault',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u6392\u5e8f'),
        ),
    ]

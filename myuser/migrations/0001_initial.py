# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 13:31
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='\u7528\u6237\u540d')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='\u90ae\u7bb1')),
                ('full_name', models.CharField(max_length=255, verbose_name='\u59d3\u540d')),
                ('tel', models.CharField(max_length=255, unique=True, verbose_name='\u7535\u8bdd')),
                ('sex', models.IntegerField(choices=[(1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3'), (3, b'\xe4\xbf\x9d\xe5\xaf\x86')], default=3)),
                ('qq', models.CharField(max_length=255, verbose_name='QQ\u53f7')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5')),
                ('avator', models.ImageField(default=None, null=True, upload_to='user/avators/', verbose_name='\u5934\u50cf')),
                ('is_member', models.BooleanField(default=False, verbose_name='\u793e\u5458')),
                ('is_fixer', models.BooleanField(default=False, verbose_name='\u4e49\u4fee\u961f')),
                ('is_staff', models.BooleanField(default=False, verbose_name='\u5458\u5de5')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u53ef\u7528')),
                ('register_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u6ce8\u518c\u65f6\u95f4')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

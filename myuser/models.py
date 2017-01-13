# coding=utf-8
from __future__ import unicode_literals

from django.contrib.auth.models import (
    UserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

from django.db import models
from django.utils import timezone

from myuser.constants import Sex_Choice


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(u'用户名', max_length=255, unique=True)
    email = models.CharField(u'邮箱', max_length=255, blank=True, null=True)
    full_name = models.CharField(u'姓名', max_length=255)
    tel = models.CharField(u'电话', max_length=255, unique=True)
    sex = models.IntegerField(choices=Sex_Choice, default=3)
    qq = models.CharField(u'QQ号', max_length=255)
    birthday = models.DateField(u'生日', null=True, blank=True)
    avator = models.ImageField('头像', upload_to='user/avators/',null=True, default=None)

    # permission
    is_member = models.BooleanField(u'社员', default=False)
    is_fixer = models.BooleanField(u'义修队', default=False)

    is_staff = models.BooleanField('员工', default=False)
    is_active = models.BooleanField('可用', default=True)

    register_time = models.DateTimeField(u'注册时间', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS_FOR_REGISTRATION = ['tel', 'qq']
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return self.full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.full_name.split()[0] if self.full_name else self.email

    def get_avator_url(self):
        return '/media/'.format(self.avator)

# Create your models here.

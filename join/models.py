# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class JoinUs(models.Model):
    name = models.CharField(max_length=255)
    student_no = models.CharField(max_length=255, blank=True)
    tel = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    major = models.CharField(max_length=255)


# Create your models here.

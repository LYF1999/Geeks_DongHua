#  coding=utf-8
from __future__ import unicode_literals

from rest_framework import permissions


class FixPermission(permissions.BasePermission):
    message = '您无权限操作'

    def has_permission(self, request, view):
        return request.user.is_fixer

    def has_object_permission(self, request, view, obj):
        return True

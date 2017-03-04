# coding=utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from myuser.models import User
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label='Password',
        help_text="要修改密码, 请用<a href=\"../password/\">这个表单</a>进行修改"
    )

    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        return self.initial['password']


class UserAdmin(DjangoUserAdmin):
    form = UserChangeForm
    list_display = ('username', 'full_name', 'tel', 'is_member')
    search_fields = ('username', 'tel', 'full_name')

    list_filter = ('is_staff', 'is_member', 'is_fixer')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'email', 'qq', 'tel', 'birthday', 'register_time')}),
        ('Permissions',
         {'fields': ('is_active', 'is_fixer', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_member')}),
    )


admin.site.register(User, UserAdmin)

# Register your models here.

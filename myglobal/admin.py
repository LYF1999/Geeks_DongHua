from django.contrib import admin

from myglobal.models import FixStatus


class FixStatusAdmin(admin.ModelAdmin):
    list_display = ('message', 'status')

admin.site.register(FixStatus, FixStatusAdmin)

# Register your models here.

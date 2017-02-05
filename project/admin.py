from django.contrib import admin
from project.models import OpenSourceProject, SoftWare


class OpenSourceProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)


class SoftWareAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)


admin.site.register(OpenSourceProject, OpenSourceProjectAdmin)
admin.site.register(SoftWare, SoftWareAdmin)

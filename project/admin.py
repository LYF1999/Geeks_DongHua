from django.contrib import admin
from project.models import OpenSourceProject, Tool


class OpenSourceProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)


class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)


admin.site.register(OpenSourceProject, OpenSourceProjectAdmin)
admin.site.register(Tool, ToolAdmin)

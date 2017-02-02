from django.contrib import admin
from project.models import OpenSourceProject


class OpenSourceProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name',)


admin.site.register(OpenSourceProject, OpenSourceProjectAdmin)

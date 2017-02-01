from django.contrib import admin

from fix.models import Fault, Fix


class FixAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'dorm_number', 'fault', 'is_fix', 'fixer')
    list_filter = ('fault', 'dorm_number')
    search_fields = ('name', 'tel')


admin.site.register(Fix, FixAdmin)
admin.site.register(Fault)
# Register your models here.

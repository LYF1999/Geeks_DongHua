from django.contrib import admin

from fix.models import Fault, Fix


class FaultAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


class FixAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'dorm_number', 'fault', 'is_fix', 'fixer', 'appointment_time')
    list_filter = ('fault', 'dorm_number')
    search_fields = ('name', 'tel')


admin.site.register(Fix, FixAdmin)
admin.site.register(Fault, FaultAdmin)
# Register your models here.

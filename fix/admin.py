from django.contrib import admin

from fix.models import Fault, Fix, Recruit


class FaultAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


class FixAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'dorm_number', 'fault', 'is_fix', 'fixer', 'appointment_time')
    list_filter = ('fault', 'dorm_number')
    search_fields = ('name', 'tel')


class RecruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'desc')


admin.site.register(Fix, FixAdmin)
admin.site.register(Fault, FaultAdmin)
admin.site.register(Recruit, RecruitAdmin)
# Register your models here.

from rest_framework import serializers
from fix.models import Fix


class AppointmentForm(serializers.ModelSerializer):
    class Meta:
        model = Fix
        exclude = ('appointment_time', 'fixer', 'fix_time')

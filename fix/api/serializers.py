from rest_framework import serializers

from fix.models import Fix, Fault


class FixSerializer(serializers.ModelSerializer):
    appointment_time = serializers.CharField(source='get_appointment_time')

    class Meta:
        model = Fix
        fields = '__all__'


class FaultSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='name')
    value = serializers.IntegerField(source='id')

    class Meta:
        model = Fault
        fields = ['label', 'value']

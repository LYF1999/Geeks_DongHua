from rest_framework import serializers

from fix.models import Fix


class FixSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fix
        fields = '__all__'

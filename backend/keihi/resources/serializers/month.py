from rest_framework import serializers
from resources.models import Month


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = '__all__'

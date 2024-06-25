from resources.models import Year

from rest_framework import serializers


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'

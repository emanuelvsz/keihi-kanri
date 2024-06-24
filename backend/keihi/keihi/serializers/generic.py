from rest_framework import serializers

class GenericIDSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)

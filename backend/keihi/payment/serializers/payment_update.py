from rest_framework import serializers
from payment.models import Payment

class PaymentUpdateSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    date = serializers.DateField(required=False, allow_null=True)
    quantity = serializers.FloatField(required=False)

    class Meta:
        model = Payment
        fields = ['id', 'description', 'date', 'quantity']

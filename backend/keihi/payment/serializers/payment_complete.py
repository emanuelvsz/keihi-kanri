from rest_framework import serializers
from payment.models import Payment

class PaymentCompleteSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=True)
    quantity = serializers.FloatField(required=True)
    
    class Meta:
        model = Payment
        fields = ['id', 'quantity']
from rest_framework import serializers
from payment.models import Payment
from datetime import date

class PaymentCreateSerializer(serializers.ModelSerializer):
    date = serializers.DateField(default=date.today, required=False)
    
    class Meta:
        model = Payment
        fields = ['date', 'description']
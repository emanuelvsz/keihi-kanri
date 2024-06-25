from django.utils.timezone import now
from payment.models import Payment


class PaymentServices:
    
    def get_all():
        return Payment.objects.all()
    
    def create(data: dict):
        object = Payment.objects.create(
            description=data.get('description', ''),
            date=data.get('date', None)
        )
        return object.id
    
    def update(data: dict):
        object = Payment.objects.filter(
            id=data.get('id')
        ).first()
        if not object:
            return None
        if not data.get('description') == object.description:
            object.description = data.get('description')
        if not str(data.get('date')) == str(object.date):
            object.date = data.get('date')
        object.save()
        return object.id
    
    def delete(id: str):
        object = Payment.objects.get(
            id=id
        )
        if not object:
            return None
        object.delete()
        return None
    
    def complete_payment(data: dict):
        object = Payment.objects.filter(
            id=data.get('id')
        ).first()
        if not object:
            return None
        object.payed_at = now()
        object.quantity = data.get('quantity')
        object.save()
        return object.id
    
    def get_payment_by_month(month_id: int):
        object = Payment.objects.filter(
            date__month=month_id
        )
        return object
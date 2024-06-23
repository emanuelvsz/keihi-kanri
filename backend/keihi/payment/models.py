from django.db import models
import uuid

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payed_at = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)
    quantity = models.FloatField()
    description = models.TextField()
    month_id = models.IntegerField()
    
    class Meta:
        db_table = "payment"
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

        indexes = [
            models.Index(fields=["id"]),
        ]
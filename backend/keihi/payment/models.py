from django.db import models
import uuid

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payed_at = models.DateTimeField(null=True, blank=True)
    quantity = models.FloatField(null=True, blank=True)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "payment"
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        unique_together = [['date']]

        indexes = [
            models.Index(fields=["id"]),
        ]
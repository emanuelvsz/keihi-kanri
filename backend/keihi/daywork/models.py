from django.db import models
from payment.models import Payment

import uuid

class Daywork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    started_at = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "daywork"
        verbose_name = "Daywork"
        verbose_name_plural = "Dayworks"

        indexes = [
            models.Index(fields=["id"]),
        ]

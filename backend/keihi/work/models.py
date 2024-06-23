from django.db import models
import uuid
from daywork.models import Daywork
# Create your models here.
class Work(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hours = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    daywork = models.ForeignKey(Daywork, on_delete=models.CASCADE)
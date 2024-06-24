from django.db import models

class Month(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "month"
        verbose_name = "Month"
        verbose_name_plural = "Months"

    def __str__(self):
        return self.name

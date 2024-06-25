from django.db import models

class Year(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = "year"
        verbose_name = "Year"
        verbose_name_plural = "Years"

    def __str__(self):
        return self.name

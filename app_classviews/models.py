from django.db import models

# Create your models here.
class Travel(models.Model):
    destination = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['date_start']
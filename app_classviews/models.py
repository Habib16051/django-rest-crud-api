from django.db import models

# Create your models here.
class Travel(models.Model):
    destination = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey('auth.User', related_name='travels', on_delete=models.CASCADE, null=True)
    highlighted = models.TextField(blank=True, default='')


    class Meta:
        ordering = ['date_start']
    def __str__(self):
        return f"{self.destination} ({self.date_start} - {self.date_end})"

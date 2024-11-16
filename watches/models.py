from django.db import models


# Modellər burada yaradılır.
class Watch(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=70)
    describtion = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField()
    discount_dedline = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.marka} - {self.model}'

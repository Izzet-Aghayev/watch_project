from django.db import models

from django.contrib.auth.models import User


# Kateqoriyalar üçün model.
class Category(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


# Modellər burada yaradılır.
class Watch(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)    # User ilə Watch modelinin əlaqəsi.
    categories = models.ManyToManyField(Category)       # Kateqoriya ilə Watch modelini qlaqələndiri.

    marka = models.CharField(max_length=50)     # Simvol limiti vermək olur.
    model = models.CharField(max_length=70)
    describtion = models.TextField()            # Simvol limiti yoxdiur.
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Qiymət üçün lazım olan fielddir.
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_dedline = models.DateField(null=True, blank=True)  # Tarixi vermək üçün fielddir.

    def __str__(self):
        return f'{self.user.username} - {self.marka}'

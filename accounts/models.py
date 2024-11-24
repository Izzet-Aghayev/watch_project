from django.db import models
from django.contrib.auth.models import User


# Profil üçün model quraq.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True) # Profillə useri əlaqələndirir, 1 user <---> 1 profil.

    about = models.TextField(null=True, blank=True)        # Limitsiz simvol istifadə edilə bilər.
    phone_num = models.CharField(max_length=20, null=True, blank=True)      # Simvol sayına limit verilir.
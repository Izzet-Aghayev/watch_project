from django.db.models.signals import post_save, pre_save, post_delete, pre_delete, pre_migrate    # Signalın tətikləndiyi hallardır.
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profile


# Bu dekorator siqnal üçündür.
@receiver(post_save, sender=User)
def creation_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(seller=instance)    # Yeni seller qeydiyyatı tamamladığı zaman ona uyğun profil yaradır.
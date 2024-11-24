from django.contrib import admin

from .models import Profile


# Bununla profilləri admin paneldən izləmək mümkündür.
admin.site.register(Profile)

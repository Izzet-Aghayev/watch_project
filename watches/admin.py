from django.contrib import admin
# Yaratdığımız modeli buraya import edirk.
from watches.models import Watch


# Modeli adminə tanıdırıq.
admin.site.register(Watch)
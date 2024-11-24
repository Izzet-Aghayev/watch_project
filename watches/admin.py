from django.contrib import admin
# Yaratdığımız modeli buraya import edirk.
from watches.models import Category, Watch


# Modeli adminə tanıdırıq.
admin.site.register(Watch)
admin.site.register(Category)
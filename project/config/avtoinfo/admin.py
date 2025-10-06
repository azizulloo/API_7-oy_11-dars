from django.contrib import admin
from .models import Brand, Car, Color

# Register your models here.

admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Car)

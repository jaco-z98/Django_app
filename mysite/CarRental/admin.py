from django.contrib import admin

from .models import Car, CarType, CarFuelType

admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(CarFuelType)
from django.contrib import admin
from core.models import Automaker, Vehicle, Modelo, Gear

# Register your models here.
admin.site.register(Automaker)
admin.site.register(Vehicle)
admin.site.register(Modelo)
admin.site.register(Gear)
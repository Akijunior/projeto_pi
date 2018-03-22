from django.contrib import admin
from buy.models import *
# Register your models here.
admin.site.register(Buy)
admin.site.register(Item)
admin.site.register(Pay)
admin.site.register(Order)
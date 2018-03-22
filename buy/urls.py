from django.urls import path
from .views import *

urlpatterns = [
    path('add_item/<int:pk>', add_item, name='add_item'),
    path('purchase_status/<int:pk>', purchase_status, name='purchase_status'),
]

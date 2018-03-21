from django.urls import path
from .views import *

urlpatterns = [
    path('add_item/<int:pk>', add_item, name='add_item'),
]

from django.urls import path
from .views import *


urlpatterns = [
    path('register_gear', register_gear, name='register_gear'),
    path('ver_peca/<int:pk>', gear, name='gear_manage'),
    path('editar_peca/<int:pk>', gear_edit, name='gear_edit'),
    path('register_model', register_model, name='register_model'),
    path('register_vehicle', register_vehicle, name='register_vehicle'),
    path('register_automaker', register_automaker, name='register_automaker'),
    path('', index, name='index'),
]
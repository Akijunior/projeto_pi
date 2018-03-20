from django.urls import path
from .views import *


urlpatterns = [
    path('register_gear', register_gear, name='register_gear'),
]
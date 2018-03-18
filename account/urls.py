from django.urls import path
from .views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    path('', login, {'template_name': 'account/login.html'}, name='login'),
    path('sair/', logout,
        {'next_page': 'login'}, name='logout'),
    path('cadastre-se/', register, name='register'),
    path('nova-senha/', password_reset, name='password_reset'),
    path('confirmar-nova-senha/<key>', password_reset_confirm, name='password_reset_confirm'),
    path('index', index, name='index'),
]
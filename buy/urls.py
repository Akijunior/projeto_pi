from django.urls import path
from .views import *

urlpatterns = [
    path('add_item/<int:pk>', add_item, name='add_item'),
    path('purchase_status/<int:pk>', purchase_status, name='purchase_status'),
    path('finalizar_compra/<int:pk>', payment, name='payment'),
    path('solicitar_pedido/<int:pk>', request_order, name='request_order'),
]

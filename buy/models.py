from django.db import models
from core.models import Gear

from django.conf import settings


class Buy(models.Model):
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Comprador', related_name='purshases',
                              on_delete=models.CASCADE)

class Item(models.Model):
    buy = models.ForeignKey('Buy', on_delete=models.CASCADE)
    item = models.ForeignKey('core.Gear', verbose_name='peça', related_name='items', on_delete=models.CASCADE)


class Pay(models.Model):
    TYPE_PAY_CHOICES = (
        ('cartao', 'Cartão'),
        ('em especie', 'Em espécie'),
        ('por boleto', 'Por boleto'),
    )
    type_pay = models.CharField(max_length=20, choices=TYPE_PAY_CHOICES, default='Em especie')
    total_value = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.ForeignKey(Buy, verbose_name='Compra', related_name='pagamento', on_delete=models.CASCADE)
    date_pay = models.DateTimeField('Data de pagamento', auto_now_add=True)


class Order(models.Model):
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='solicitante',
        related_name='solicitacoes', on_delete=models.CASCADE
    )
    item = models.ForeignKey('core.Gear', verbose_name='peça', related_name='solicitacoes', on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)

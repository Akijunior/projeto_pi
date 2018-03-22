from django.db import models
from core.models import Gear

from django.conf import settings


class Buy(models.Model):
    BUY_STATUS = (
        ('open', 'Aberta'),
        ('closed', 'Fechada'),
    )
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Comprador', related_name='purshases',
                              on_delete=models.CASCADE)
    amount_items = models.IntegerField('Quantidade de itens', default=0)
    status = models.CharField(max_length=5, choices=BUY_STATUS, default='closed')
    created_at = models.DateTimeField('Iniciada em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizada em', auto_now=True)

    def __str__(self):
        return "Comprador: " + str(self.buyer) + " | Status: " + str(self.get_status_display())

class Item(models.Model):
    buy = models.ForeignKey('Buy', related_name='items',on_delete=models.CASCADE)
    gear = models.ForeignKey('core.Gear', verbose_name='peça', related_name='item', on_delete=models.CASCADE)
    amount = models.IntegerField('Quantidade', default=0)

    def __str__(self):
        return str(self.gear) + " X " + str(self.amount)


class Pay(models.Model):
    TYPE_PAY_CHOICES = (
        ('cartao', 'Cartão'),
        ('em especie', 'Em espécie'),
        ('por boleto', 'Por boleto'),
    )
    type_pay = models.CharField(max_length=20, choices=TYPE_PAY_CHOICES, default='Em especie')
    date_pay = models.DateTimeField('Data de pagamento', auto_now_add=True)
    total_value = models.FloatField('Valor total do pagamento', null=True, blank=True)
    buy = models.ForeignKey(Buy, verbose_name='Compra', related_name='pagamento', on_delete=models.CASCADE)



class Order(models.Model):
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='solicitante',
        related_name='solicitacoes', on_delete=models.CASCADE
    )
    item = models.ForeignKey('core.Gear', verbose_name='peça', related_name='solicitacoes', on_delete=models.CASCADE)
    date_order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Solicitante: %s | Data da solicitação: %s" % (str(self.requester), str(self.date_order))

def post_buy_save_reply(instance, **kwargs):
    m_buy = Buy.objects.get(pk=instance.buy.id)
    m_buy.amount_items = 0
    for item in m_buy.items.all():
        m_buy.amount_items += item.amount
    m_buy.save()

models.signals.post_save.connect(
    post_buy_save_reply, sender=Item, dispatch_uid='post_buy_save_reply'
)
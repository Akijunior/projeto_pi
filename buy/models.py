from django.db import models
from buy.models import Gear, Accessory, Buy

class Buy(models.Model):
	total_value = models.DecimalField(max_digits=5, decimal_places=2)
	buyer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Comprador', related_name='compras', on_delete=models.CASCADE)

class Pay(models.Model):
	TYPE_PAY_CHOICES = (
		('cartao', 'Cartão'),
		('em especie', 'Em espécie'),
		('por boleto', 'Por boleto'),
	)
	type_pay = models.CharField(max_length=20, choices=TYPE_PAY_CHOICES, default='Em especie')
	total_value = models.DecimalField(max_digits=5, decimal_places=2)
	buy = models.ForeignKey(Buy, verbose_name='Compra', related_name='pagamento', on_delete=models.CASCADE)

class Order(models.Model):
	requester = models.ForeignKey(
		settings.AUTH_USER_MODEL, verbose_name='solicitante',
		related_name='solicitacoes', on_delete=models.CASCADE
	)
	item = models.ForeignKey(Gear, verbose_name='peça', related_name='solicitacoes', on_delete=models.CASCADE)
	date_order = models.DateTimeField(auto_now_add=True)
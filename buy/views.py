from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from buy.models import Item, Buy
from core.models import Gear


def add_item(request, pk):
    user = request.user
    gear = get_object_or_404(Gear, pk=pk)
    # Caso a compra se inicie agora
    if user.purshases.filter(status='open').count() == 0:
        buy = Buy(buyer=user, status='open')
    # Caso a compra ja estivesse em andamento
    else:
        buy = user.purshases.get(status='open')
    if Item.objects.filter(gear=gear, buy=buy).exists():
        item = Item.objects.get(gear=gear, buy=buy)
    else:
        item = Item(gear=gear, buy=buy)
    item.amount += 1
    item.save()
    messages.success(request, 'Um novo %s foi adicionado com sucesso ao seu carrinho' % str(item.gear.name_descr))
    return redirect('index')

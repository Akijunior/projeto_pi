from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from buy.forms import PayForm
from buy.models import Item, Buy, Order
from buy.search_fuzzy import get_search_matches
from core.models import Gear

def request_order(request, pk):
    gear = get_object_or_404(Gear, pk=pk)
    order = Order(requester=request.user, item=gear)
    order.save()
    messages.success(request, 'Uma solicitação de %s foi feita com sucesso para você' % str(gear.name_descr))
    return redirect('index')

def add_item(request, pk):
    user = request.user
    gear = get_object_or_404(Gear, pk=pk)
    # Caso a compra se inicie agora
    if user.purshases.filter(status='open').count() == 0:
        buy = Buy(buyer=user, status='open')
        buy.save()
    # Caso a compra ja estivesse em andamento
    else:
        buy = user.purshases.get(status='open')
        
        #print('kkkkkkkkkk > '+str(buy.id))
    if Item.objects.filter(gear=gear, buy=buy).exists():
        item = Item.objects.get(gear=gear, buy=buy)
    else:
        item = Item(gear=gear, buy=buy)
    item.amount += 1
    item.save()
    messages.success(request, 'Um novo %s foi adicionado com sucesso ao seu carrinho' % str(item.gear.name_descr))
    return redirect('index')


def purchase_status(request, pk):
    buy = get_object_or_404(Buy, pk=pk)
    total_value = 0
    for item in buy.items.all():
        if item.amount:
            total_value += item.gear.price * item.amount
        else:
            total_value += item.gear.price
    return render(request, 'buy/purchase_status.html', {'buy': buy, 'total':total_value})

@login_required
def register_payment(request):
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão de acessar essa página')
        return redirect('index')
    

def payment(request, pk):
    buy = get_object_or_404(Buy, pk=pk)
    form = PayForm(request.POST or None)
    if form.is_valid():
        modelo = form.save(commit=False)
        m_total_value = 0
        for item in buy.items.all():
            m_total_value += item.gear.price * item.amount
            item.gear.amount -= item.amount
            item.gear.save()
        modelo.buy = buy
        modelo.total_value = m_total_value
        modelo.save()
        messages.success(request, 'Pagamento efetuado.')
        buy.status = 'closed'
        buy.save()
        return redirect('index')
    context = {
        'buy': buy,
        'form': form,
    }
    return render(request, 'buy/payment_page.html', context)
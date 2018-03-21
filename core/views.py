from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext

from core.forms import GearUploadForm
from core.models import Gear


def index(request):
    context = {
        'gears': Gear.objects.all(),
        'product': gettext("Mensagem de produto"),
        'message': gettext("Nova mensagem de produto"),
    }
    return render(request, 'index.html', context)

def register_gear(request):
    form = GearUploadForm(request.POST or None, request.FILES)
    if form.is_valid():
        gear = form.save(commit=False)
        gear.save()
        messages.success(request, 'A nova peça foi adicionada com sucesso.')
        return redirect('index')
    template_name = 'register_gear.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)




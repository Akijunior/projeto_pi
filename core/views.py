from django.contrib import messages
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect

# Create your views here.
from core.forms import GearUploadForm


def register_gear(request):
    form = GearUploadForm(request.POST or None, request.FILES)
    if form.is_valid():
        gear = form.save(commit=False)
        gear.save()
        messages.success(request, 'A nova peça foi adicionada com sucesso.')
        redirect('index')
    template_name = 'register_gear.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)




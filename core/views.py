from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext
from django.views.generic import DetailView

from buy.models import Buy, Item
from core.forms import GearForm, ModeloForm, VehicleForm, AutomakerForm
from core.models import Gear


def index(request):
    context = {
        'gears': Gear.objects.all(),
        'product': gettext("Mensagem de produto"),
        'message': gettext("Nova mensagem de produto"),
    }
    if request.user.is_authenticated and Buy.objects.filter(buyer=request.user, status='open').exists():
        context['buy'] = Buy.objects.get(buyer=request.user, status='open')
    return render(request, 'index.html', context)


@login_required
def register_gear(request):
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão de acessar essa página')
        return redirect('index')
    form = GearForm(request.POST or None, request.FILES)
    if form.is_valid():
        gear = form.save(commit=False)
        gear.save()
        messages.success(request, 'A nova peça foi adicionada com sucesso')
        return redirect('index')
    template_name = 'register_gear.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def register_model(request):
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão de acessar essa página')
        return redirect('index')
    form = ModeloForm(request.POST or None)
    if form.is_valid():
        modelo = form.save(commit=False)
        modelo.save()
        messages.success(request, 'O novo modelo foi adicionado com sucesso.')
        return redirect('index')
    template_name = 'register_model.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def register_vehicle(request):
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão de acessar essa página')
        return redirect('index')
    form = VehicleForm(request.POST or None)
    if form.is_valid():
        vehicle = form.save(commit=False)
        vehicle.save()
        messages.success(request, 'O novo veículo foi adicionado com sucesso.')
        return redirect('index')
    template_name = 'register_vehicle.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def register_automaker(request):
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão de acessar essa página')
        return redirect('index')
    form = AutomakerForm(request.POST or None)
    if form.is_valid():
        automaker = form.save(commit=False)
        automaker.save()
        messages.success(request, 'A nova montadora foi adicionada com sucesso.')
        return redirect('index')
    template_name = 'register_automaker.html'
    context = {
        'form': form,
    }
    return render(request, template_name, context)


class GearView(DetailView):
    model = Gear
    template_name = 'gear_manage.html'

    def get(self, request, *args, **kwargs):
        response = super(GearView, self).get(request, *args, **kwargs)
        self.object.views += 1
        self.object.save()
        return response

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            messages.error(self.request, 'Você não tem permissão de acessar essa página')
            return redirect(self.request.path)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        if form.is_valid():
            gear = form.save(commit=False)
            gear.save()
            messages.success(self.request, 'A sua mensagem foi enviada com sucesso')
            context['form'] = GearForm()
        return self.render_to_response(context)


gear = GearView.as_view()


def gear_edit(request, pk):
    if not request.user.is_staff:
        messages.error(request, 'Você não tem permissão de acessar essa página')
        return redirect('index')
    gear = get_object_or_404(Gear, pk=pk)
    if request.method == "POST":
        form = GearForm(request.POST, instance=gear)
        if form.is_valid():
            gear = form.save(commit=False)
            gear.save()
            messages.success(request, 'A alteração em %s foi feita com sucesso' % gear.name_descr)
            return redirect('index')
    else:
        form = GearForm(instance=gear)
    return render(request, 'gear_edit.html', {'form': form})

def acessorios(request):
    context = {
        'gears': Gear.objects.filter(type_gear='acessórios'),
    }
    if request.user.is_authenticated and Buy.objects.filter(buyer=request.user, status='open').exists():
        context['buy'] = Buy.objects.get(buyer=request.user, status='open')
    return render(request, 'index.html', context)

def roda(request):
    context = {
        'gears': Gear.objects.filter(type_gear='roda'),
    }
    if request.user.is_authenticated and Buy.objects.filter(buyer=request.user, status='open').exists():
        context['buy'] = Buy.objects.get(buyer=request.user, status='open')
    return render(request, 'index.html', context)

def iluminacao(request):
    context = {
        'gears': Gear.objects.filter(type_gear='iluminação'),
    }
    if request.user.is_authenticated and Buy.objects.filter(buyer=request.user, status='open').exists():
        context['buy'] = Buy.objects.get(buyer=request.user, status='open')
    return render(request, 'index.html', context)

def multimidia(request):
    context = {
        'gears': Gear.objects.filter(type_gear='multimidia'),
    }
    if request.user.is_authenticated and Buy.objects.filter(buyer=request.user, status='open').exists():
        context['buy'] = Buy.objects.get(buyer=request.user, status='open')
    return render(request, 'index.html', context)

def seguranca(request):
    context = {
        'gears': Gear.objects.filter(type_gear='segurança'),
    }
    if request.user.is_authenticated and Buy.objects.filter(buyer=request.user, status='open').exists():
        context['buy'] = Buy.objects.get(buyer=request.user, status='open')
    return render(request, 'index.html', context)

def grades(request):
    context = {
        'gears': Gear.objects.filter(type_gear='grades'),
    }
    if request.user.is_authenticated and Buy.objects.filter(buyer=request.user, status='open').exists():
        context['buy'] = Buy.objects.get(buyer=request.user, status='open')
    return render(request, 'index.html', context)

def motocicletas(request):
    context = {
        'gears': Gear.objects.filter(type_gear='motocicletas'),
    }
    if request.user.is_authenticated and Buy.objects.filter(buyer=request.user, status='open').exists():
        context['buy'] = Buy.objects.get(buyer=request.user, status='open')
    return render(request, 'index.html', context)

def aumentar_qtd(request, pk):
    item = get_object_or_404(Item, pk=pk)
    gear = get_object_or_404(Gear, pk=item.gear)
    item.amount += 1
    item.save()
    context = {
        'item': item,
        'gear': gear,
    }
    context['total'] = gear.price * item.amount
    if request.user.is_authenticated and Buy.objects.filter(buyer=request.user, status='open').exists():
        context['buy'] = Buy.objects.get(buyer=request.user, status='open')
    return render(request, 'index.html', context)
from django import forms

from core.models import Gear, Automaker, Modelo, Vehicle


class GearForm(forms.ModelForm):
    class Meta:
        model = Gear
        exclude = ['views']

class AutomakerForm(forms.ModelForm):
    class Meta:
        model = Automaker
        fields = '__all__'

class ModeloForm(forms.ModelForm):
    class Meta:
        model = Modelo
        fields = '__all__'

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'


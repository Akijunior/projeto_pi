from django import forms

from core.models import Gear


class GearUploadForm(forms.ModelForm):
    class Meta:
        model = Gear
        exclude = ['views']


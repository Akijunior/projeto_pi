from django import forms

from buy.models import Pay


class PayForm(forms.ModelForm):
    class Meta:
        model = Pay
        exclude = ['buy', 'total_value']

class SearchForm(forms.Form):
    search =forms.CharField(label='Faça sua pesquisa aqui', max_length=100)
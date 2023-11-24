from django import forms
from aluno.models import Hospedagem


class HospedagemForm(forms.ModelForm):
    class Meta:
        model = Hospedagem
        fields = '__all__'
        widgets = [
            {'data_entrada': forms.DateInput(
                attrs={'class': 'form-control', 'format': '%Y-%m-%d'})},
            {'data_saida': forms.DateInput(
                attrs={'class': 'form-control', 'format': '%Y-%m-%d'})},
            {'valor': forms.NumberInput(attrs={'class': 'form-control'})},
            {'cliente': forms.Select(attrs={'class': 'form-control'})},
            {'quarto': forms.Select(attrs={'class': 'form-control'})},
        ]

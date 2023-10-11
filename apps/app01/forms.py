from django import forms
from .models import Dados

class DadosForm(forms.ModelForm):
    class Meta:
        model = Dados
        fields = ['nome','telefone','email','cidade','subestacao','nivel_tensao_AT','nivel_tensao_BT']
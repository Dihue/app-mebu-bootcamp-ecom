from django import forms

from .models import Cuenta


class FormCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['saldo', 'estado']

from django import forms

from .models import Cuenta


class FormCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['saldo', 'estado']


class IngresoDineroForm(forms.ModelForm):
    cantidad = forms.DecimalField(
        max_digits=12, decimal_places=2,
        label='Cantidad a ingresar',
        min_value=0, initial=0)

    class Meta:
        model = Cuenta
        fields = ['cantidad']
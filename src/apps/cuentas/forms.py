from django import forms

from .models import Cuenta, CuentaFrecuente


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


class CuentaFrecuenteForm(forms.ModelForm):
    class Meta:
        model = CuentaFrecuente
        fields = ['cuenta', 'alias']

    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['cuenta'].queryset = Cuenta.objects.exclude(usuario=user)

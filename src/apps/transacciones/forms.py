from django import forms

from .models import Transaccion


class FormTransaccion(forms.ModelForm):
    receptor_username = forms.CharField(label='Nombre de usuario del receptor')
    monto = forms.DecimalField(max_digits=12, decimal_places=2, min_value=0.01, label='Monto a transferir')

    class Meta:
        model = Transaccion
        fields = ['monto', 'motivo']

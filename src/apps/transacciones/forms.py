from django import forms

from .models import Transaccion


class FormTransaccion(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['emisor', 'receptor', 'motivo', 'monto', 'fecha']


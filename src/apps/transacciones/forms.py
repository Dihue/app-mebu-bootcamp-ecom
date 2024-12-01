from django import forms

from .models import Transaccion

from apps.motivos.models import Motivo


class FormTransaccion(forms.Form):
    receptor_username = forms.CharField(label='Nombre de usuario del receptor')
    monto = forms.DecimalField(max_digits=12, decimal_places=2, min_value=0.00, label='Monto a transferir')
    motivo = forms.ModelChoiceField(queryset=Motivo.objects.all(), label='Motivo de la transferencia')

    class Meta:
        model = Transaccion
        fields = ['monto', 'motivo']
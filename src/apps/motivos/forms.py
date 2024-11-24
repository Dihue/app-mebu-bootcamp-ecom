from django import forms

from .models import Motivo


class FormTransaccion(forms.ModelForm):
    class Meta:
        model = Motivo
        fields = ['descripcion']


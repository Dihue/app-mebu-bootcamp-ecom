from django import forms

from .models import Motivo


class FormTransaccion(forms.ModelForm):
    class Meta:
        model = Motivo
        fields = ['descripcion']


class MotivoForm(forms.ModelForm):
    class Meta:
        model = Motivo
        fields = ['descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario


class FormUsuario(UserCreationForm):

    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'dni',
            'foto_perfil'
        ]
    

class UsuarioFilterForm(forms.Form):
    q = forms.CharField(
        required=False,
        label="Buscar",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Por nombre o apellido',
        })
    )


class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'dni', 'is_active']
        widgets = {
            'is_active': forms.CheckboxInput(),
        }

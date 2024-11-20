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
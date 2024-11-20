from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import FormUsuario
from .models import Usuario

class Nuevo(CreateView):
    template_name = 'usuarios/nuevo.html'
    model = Usuario
    form_class = FormUsuario
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        ctx = super(Nuevo, self).get_context_data(**kwargs)
        ctx["titulo"] = "Nuevo registro"
        ctx["subtitulo"] = "Registro"
        return ctx

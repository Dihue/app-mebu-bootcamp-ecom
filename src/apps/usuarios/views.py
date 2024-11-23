from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy

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


class UsuarioDetalles(DetailView):
    model = Usuario
    template_name = 'usuarios/detalle.html'
    context_object_name = 'usuario'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioDetalles, self).get_context_data(**kwargs)
        ctx["titulo"] = "Detalles del Usuario"
        ctx["subtitulo"] = "Detalles"
        return ctx


class Lista(ListView):
    template_name = 'usuarios/lista.html'
    model = Usuario
    context_object_name = 'usuario'
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        ctx = super(Lista, self).get_context_data(**kwargs)
        ctx["titulo"] = "Lista de Usuarios"
        return ctx


class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['first_name', 'last_name', 'dni', 'email', 'foto_perfil']
    template_name = 'usuarios/editar.html'
    context_object_name = 'usuario'

    def get_context_data(self, **kwargs):
        ctx = super(UsuarioUpdate, self).get_context_data(**kwargs)
        ctx["titulo"] = "Editar datos"
        return ctx
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse('usuarios:detalle', kwargs={'id': self.request.user.pk})

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

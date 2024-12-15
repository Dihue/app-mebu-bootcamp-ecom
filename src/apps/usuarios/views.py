from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy

from .forms import FormUsuario, UsuarioFilterForm
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
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', '')  # 'q' es el nombre del campo del formulario
        if search_query:
            # Filtrar por nombre o apellido
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        ctx = super(Lista, self).get_context_data(**kwargs)
        ctx["titulo"] = "Lista de Usuarios"
        ctx["subtitulo"] = "Lista de Usuarios"
        ctx['formulario_buscador'] = UsuarioFilterForm(self.request.GET or None)
        return ctx


def buscar_usuarios(request):
    query = request.GET.get('q', '')
    resultados = Usuario.objects.filter(
        Q(first_name__icontains=query) |
        Q(last_name__icontains=query)
    ).values('id', 'first_name', 'last_name')  # Devuelve solo los campos necesarios
    return JsonResponse(list(resultados), safe=False)


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


User = get_user_model()

class AdminUserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Usuario
    template_name = 'usuarios/admin_user_list.html'
    context_object_name = 'usuarios'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) | 
                Q(last_name__icontains=search_query)
            )
        return queryset

    def test_func(self):
        user = self.request.user
        print(f"Superusuario: {user.is_superuser}, Grupo Administradores: {user.groups.filter(name='Administradores').exists()}")
        return user.is_superuser or user.groups.filter(name='Administradores').exists()


    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        ctx['es_admin'] = user.is_superuser or user.groups.filter(name='Administradores').exists()
        return ctx

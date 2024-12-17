from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import FormUsuario, UsuarioFilterForm, EditarUsuarioForm
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
        return super().form_valid(form)


User = get_user_model()

class AdminUserListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Usuario
    template_name = 'usuarios/admin_user_list.html'
    context_object_name = 'usuarios'
    paginate_by = 3

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
        return user.is_superuser or user.groups.filter(name='Administradores').exists()


    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user = self.request.user
        ctx['es_admin'] = user.is_superuser or user.groups.filter(name='Administradores').exists()
        ctx['formulario_buscador'] = UsuarioFilterForm(self.request.GET or None)
        ctx["titulo"] = "Administración de Usuarios"
        ctx["subtitulo"] = "Administración"
        return ctx


@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='Administradores').exists())
def toggle_user_active(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)
    usuario.is_active = not usuario.is_active
    usuario.save()
    estado = "activado" if usuario.is_active else "desactivado"
    messages.success(request, f"El usuario {usuario} ha sido {estado}.")
    return redirect('usuarios:admin_user_list')


class EditarUsuarioView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Usuario
    form_class = EditarUsuarioForm
    template_name = 'usuarios/admin_user_edit.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Administradores').exists()

    def get_success_url(self):
        return reverse('usuarios:admin_user_list')


class DetalleUsuarioView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Usuario
    template_name = 'usuarios/admin_user_detail.html'
    context_object_name = 'usuario'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Administradores').exists()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        cuenta = getattr(self.object, 'cuenta', None)  # Obtener la cuenta del usuario
        ctx['cuenta'] = cuenta
        ctx["titulo"] = "Detalles de la Cuenta"
        ctx["subtitulo"] = "Detalles"

        # Obtener todas las transacciones relacionadas (emitidas y recibidas)
        if cuenta:
            transacciones_emitidas = cuenta.transacciones_emitidas.all()
            transacciones_recibidas = cuenta.transacciones_recibidas.all()
            ctx['transacciones'] = transacciones_emitidas.union(transacciones_recibidas).order_by('-fecha')
        else:
            ctx['transacciones'] = []

        return ctx


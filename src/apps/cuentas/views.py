from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .forms import FormCuenta, IngresoDineroForm, CuentaFrecuenteForm
from .models import Cuenta, CuentaFrecuente

from apps.transacciones.models import Transaccion
from apps.motivos.models import Motivo

class Nuevo(LoginRequiredMixin, CreateView):
    template_name = 'cuentas/nuevo.html'
    model = Cuenta
    form_class = FormCuenta
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        ctx = super(Nuevo, self).get_context_data(**kwargs)
        ctx["titulo"] = "Nueva cuenta"
        ctx["subtitulo"] = "Cuenta"
        return ctx
    
    def form_valid(self, form):
        if Cuenta.objects.filter(usuario=self.request.user).exists():
            form.add_error(None, 'El usuario ya tiene una cuenta asociada.')
            return self.form_invalid(form)
        form.instance.usuario = self.request.user
        return super(Nuevo, self).form_valid(form)


class CuentaDetalles(DetailView):
    model = Cuenta
    template_name = 'cuentas/detalle.html'
    context_object_name = 'cuenta'
    
    def get_object(self, queryset=None):
        return self.request.user.cuenta

    def get_context_data(self, **kwargs):
        ctx = super(CuentaDetalles, self).get_context_data(**kwargs)
        ctx["titulo"] = "Cuenta"
        ctx["subtitulo"] = "Detalles"
        return ctx


class IngresoDineroView(LoginRequiredMixin, UpdateView):
    model = Cuenta
    form_class = IngresoDineroForm
    template_name = 'cuentas/ingreso_dinero.html'
    
    def form_valid(self, form):
        cuenta = form.save(commit=False)
        cantidad = form.cleaned_data['cantidad']
        cuenta.saldo += cantidad
        cuenta.save()

        # Registrar el ingreso como una transacción
        motivo = Motivo.objects.get(descripcion="Ingreso de dinero")

        Transaccion.objects.create(
            tipo='ingreso',
            receptor=cuenta,
            monto=cantidad,
            motivo=motivo
        )

        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user.cuenta
    
    def get_success_url(self):
        return reverse('cuentas:detalle')
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["titulo"] = "Cuenta"
        ctx["subtitulo"] = "Ingresar Dinero"
        return ctx
    

class AgregarCuentaFrecuente(LoginRequiredMixin, CreateView):
    model = CuentaFrecuente
    form_class = CuentaFrecuenteForm
    template_name = 'cuentas/agregar_cuenta_frecuente.html'
    success_url = reverse_lazy('cuentas:lista_cuentas_frecuentes')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        # Verificar duplicados
        if CuentaFrecuente.objects.filter(usuario=self.request.user, cuenta=form.cleaned_data['cuenta']).exists():
            form.add_error('cuenta', 'Esta cuenta ya está en tu lista de frecuentes.')
            return self.form_invalid(form)

        form.instance.usuario = self.request.user
        return super().form_valid(form)


class ListaCuentasFrecuentes(LoginRequiredMixin, ListView):
    model = CuentaFrecuente
    template_name = 'cuentas/lista_cuenta_frecuente.html'
    context_object_name = 'cuentas_frecuentes'

    def get_queryset(self):
        return CuentaFrecuente.objects.filter(usuario=self.request.user)


class EliminarCuentaFrecuente(LoginRequiredMixin, DeleteView):
    model = CuentaFrecuente
    template_name = 'cuentas/eliminar_cuenta_frecuente.html'
    success_url = reverse_lazy('cuentas:lista_cuentas_frecuentes')

    def get_queryset(self):
        # Asegurarse de que el usuario solo pueda eliminar sus propias cuentas frecuentes
        return CuentaFrecuente.objects.filter(usuario=self.request.user)
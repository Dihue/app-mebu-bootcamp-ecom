from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import FormCuenta
from .models import Cuenta

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
        ctx["titulo"] = "Detalles de la Cuenta"
        ctx["subtitulo"] = "Detalles"
        return ctx
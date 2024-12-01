from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from .models import Transaccion
from .forms import FormTransaccion

from apps.cuentas.models import Cuenta

class NuevaTransaccion(LoginRequiredMixin, FormView):
    template_name = 'transaccion/nueva.html'
    model = Transaccion
    form_class = FormTransaccion
    success_url = reverse_lazy('cuentas:detalle')

    def form_valid(self, form):
        cuenta_emisor = self.request.user.cuenta
        receptor_username = form.cleaned_data['receptor_username']
        monto = form.cleaned_data['monto']
        motivo = form.cleaned_data['motivo']

        # Buscar la cuenta del receptor por su nombre de usuario
        cuenta_receptor = get_object_or_404(Cuenta, usuario__username=receptor_username)

        # Verificar que ambas cuentas estén activas
        if not cuenta_emisor.estado or not cuenta_receptor.estado:
            messages.error(self.request, 'Ambas cuentas deben estar activas para realizar la transferencia.')
            return self.form_invalid(form)

        # Verificar si hay saldo suficiente en la cuenta del emisor
        if cuenta_emisor.saldo < monto:
            messages.error(self.request, 'Saldo insuficiente para la transferencia.')
            return self.form_invalid(form)

        # Realizar la transferencia
        cuenta_emisor.saldo -= monto
        cuenta_receptor.saldo += monto
        cuenta_emisor.save()
        cuenta_receptor.save()

        # Registrar la transacción
        Transaccion.objects.create(
            emisor=cuenta_emisor,
            receptor=cuenta_receptor,
            monto=monto,
            motivo=motivo
        )

        messages.success(self.request, 'Transferencia realizada con éxito.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(NuevaTransaccion, self).get_context_data(**kwargs)
        ctx["titulo"] = "Nueva transacción"
        ctx["subtitulo"] = "Transacción"
        return ctx


class ComprobanteTransaccion(DetailView):
    model = Transaccion
    template_name = 'transaccion/comprobante.html'
    context_object_name = 'transaccion'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filtrar para que solo el emisor o receptor puedan ver la transacción
        return queryset.filter(Q(emisor__usuario=self.request.user) | Q(receptor__usuario=self.request.user))
    
    def dispatch(self, request, *args, **kwargs):
        transaccion = self.get_object()
        if transaccion.emisor.usuario != request.user and transaccion.receptor.usuario != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ListaTransacciones(LoginRequiredMixin, ListView):
    model = Transaccion
    template_name = 'transaccion/lista.html'
    context_object_name = 'transacciones'

    def get_queryset(self):
        # Filtrar transacciones para mostrar solo las relacionadas con el usuario actual
        return Transaccion.objects.filter(
            Q(emisor__usuario=self.request.user) | Q(receptor__usuario=self.request.user)
        )
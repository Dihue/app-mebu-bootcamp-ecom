from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import FormTransaccion
from .models import Transaccion

class NuevaTransaccion(LoginRequiredMixin, CreateView):
    template_name = 'transaccion/nueva.html'
    model = Transaccion
    form_class = FormTransaccion
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        ctx = super(NuevaTransaccion, self).get_context_data(**kwargs)
        ctx["titulo"] = "Nueva transacción"
        ctx["subtitulo"] = "Transacción"
        return ctx
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import FormTransaccion
from .models import Motivo

class NuevoMotivo(LoginRequiredMixin, CreateView):
    template_name = 'motivo/nuevo.html'
    model = Motivo
    form_class = FormTransaccion
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        ctx = super(NuevoMotivo, self).get_context_data(**kwargs)
        ctx["titulo"] = "Nuevo motivo"
        ctx["subtitulo"] = "Motivo"
        return ctx
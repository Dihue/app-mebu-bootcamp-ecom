from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import FormTransaccion, MotivoForm
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


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.groups.filter(name='Administradores').exists()


class MotivoListView(AdminRequiredMixin, ListView):
    model = Motivo
    template_name = 'motivo/motivo_list.html'
    context_object_name = 'motivos'


class MotivoCreateView(AdminRequiredMixin, CreateView):
    model = Motivo
    form_class = MotivoForm
    template_name = 'motivo/motivo_form.html'
    success_url = reverse_lazy('motivo:motivo_list')


class MotivoUpdateView(AdminRequiredMixin, UpdateView):
    model = Motivo
    form_class = MotivoForm
    template_name = 'motivo/motivo_form.html'
    success_url = reverse_lazy('motivo:motivo_list')


class MotivoDeleteView(AdminRequiredMixin, DeleteView):
    model = Motivo
    template_name = 'motivo/motivo_confirm_delete.html'
    success_url = reverse_lazy('motivo:motivo_list')

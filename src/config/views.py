from django.views.generic import TemplateView


class BaseTemplateView(TemplateView):
    template_name = 'inicio.html'


    def get_context_data(self, **kwargs):
        ctx = super(BaseTemplateView, self).get_context_data(**kwargs)
        ctx['titulo'] = 'Inicio'

        return ctx
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView


class BaseTemplateView(TemplateView):
    template_name = 'inicio.html'


    def get_context_data(self, **kwargs):
        ctx = super(BaseTemplateView, self).get_context_data(**kwargs)
        ctx['titulo'] = 'Bienvenido a M.E.B.U.'
        ctx['subtitulo'] = 'Inicio'
        return ctx


class LoginTempletaView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
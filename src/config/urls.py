from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as views_django
from django.urls import path, include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.BaseTemplateView.as_view(), name='inicio'),

    path('login/', views.LoginTempletaView.as_view(), name='login'),
    path('logout/', views_django.logout_then_login, name='logout'),

    #TODO: habilitar luego de los MVT de cada app
    path('cuentas/', include('apps.cuentas.urls')),
    # path('motivos/', include('apps.motivos.urls')),
    path('transacciones/', include('apps.transacciones.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
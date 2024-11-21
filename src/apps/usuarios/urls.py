from django.urls import path

from . import views

app_name = 'usuarios'


urlpatterns = [
    path('nuevo/', views.Nuevo.as_view(), name='nuevo'),
    path('lista/', views.Lista.as_view(), name='lista'),
    path('usuario/<int:id>/', views.UsuarioDetalles.as_view(), name='detalle'),
]

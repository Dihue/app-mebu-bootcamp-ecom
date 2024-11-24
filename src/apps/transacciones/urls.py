from django.urls import path

from . import views

app_name = 'transaccion'


urlpatterns = [
    path('nueva/', views.NuevaTransaccion.as_view(), name='nueva'),
]

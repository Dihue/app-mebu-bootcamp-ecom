from django.urls import path

from . import views

app_name = 'transaccion'


urlpatterns = [
    path('nueva/', views.NuevaTransaccion.as_view(), name='nueva'),
    path('comprobante/<int:pk>/', views.ComprobanteTransaccion.as_view(), name='comprobante'),
    path('transacciones/', views.ListaTransacciones.as_view(), name='lista'),
]

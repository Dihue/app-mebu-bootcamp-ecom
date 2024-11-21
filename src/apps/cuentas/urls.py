from django.urls import path

from . import views

app_name = 'cuentas'


urlpatterns = [
    path('nuevo/', views.Nuevo.as_view(), name='nuevo')
]

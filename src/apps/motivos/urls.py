from django.urls import path

from . import views

app_name = 'motivo'


urlpatterns = [
    path('nuevo/', views.NuevoMotivo.as_view(), name='nuevo'),
]

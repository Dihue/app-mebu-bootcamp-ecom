from django.urls import path

from . import views

app_name = 'motivo'


urlpatterns = [
    path('nuevo/', views.NuevoMotivo.as_view(), name='nuevo'),
    path('', views.MotivoListView.as_view(), name='motivo_list'),
    path('crear/', views.MotivoCreateView.as_view(), name='motivo_create'),
    path('editar/<int:pk>/', views.MotivoUpdateView.as_view(), name='motivo_update'),
    path('eliminar/<int:pk>/', views.MotivoDeleteView.as_view(), name='motivo_delete'),
]
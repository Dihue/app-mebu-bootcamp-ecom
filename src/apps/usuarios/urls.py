from django.urls import path

from . import views

app_name = 'usuarios'


urlpatterns = [
    path('nuevo/', views.Nuevo.as_view(), name='nuevo'),
    path('lista/', views.Lista.as_view(), name='lista'),
    path('usuario/<int:id>/', views.UsuarioDetalles.as_view(), name='detalle'),
    path('usuario/editar/', views.UsuarioUpdate.as_view(), name='editar'),

    path('buscar/', views.buscar_usuarios, name='buscar_usuarios'),
    path('admin/usuarios/', views.AdminUserListView.as_view(), name='admin_user_list'),
]

from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def configurar_grupo_administradores(sender, **kwargs):
    """
    Configura el grupo 'Administradores' y asigna los permisos necesarios.
    Este signal se ejecuta después de cada migración.
    """
    # Crear o recuperar el grupo de administradores
    grupo_admin, creado = Group.objects.get_or_create(name="Administradores")

    # Lista de nombres de permisos que queremos asignar
    permisos_codename = [
        "view_user",         # Permiso para visualizar usuarios
        "view_cuenta",       # Permiso para visualizar cuentas
        "view_transaccion",  # Permiso para visualizar transacciones
    ]

    # Obtener los permisos basándonos en sus codenames
    permisos = Permission.objects.filter(codename__in=permisos_codename)

    # Asignar los permisos al grupo
    grupo_admin.permissions.set(permisos)
    grupo_admin.save()

    print("Grupo 'Administradores' configurado con permisos:", permisos_codename)

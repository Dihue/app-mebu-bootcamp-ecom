from django.contrib.auth.models import Group

def es_admin_context(request):
    if request.user.is_authenticated:
        es_admin = request.user.is_superuser or request.user.groups.filter(name='Administradores').exists()
        return {'es_admin': es_admin}
    return {'es_admin': False}

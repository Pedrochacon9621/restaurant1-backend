from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Permite acceso solo a usuarios con rol 'Admin' (id_rol = 1).
    No verifica autenticación — se espera que IsAuthenticated lo haga.
    """
    def has_permission(self, request, view):
        return (
            hasattr(request.user, 'rol') and
            request.user.rol is not None and
            request.user.rol.id_rol == 1
        )


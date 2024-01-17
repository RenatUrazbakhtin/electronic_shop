from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """
    Проверка является ли пользователь активным
    """
    def has_permission(self, request, view):
        return request.user.is_active
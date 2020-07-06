from rest_framework import permissions

class IsAdminorReadonly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        admin_or_not = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or admin_or_not
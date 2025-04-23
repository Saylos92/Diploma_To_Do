from rest_framework.permissions import IsAuthenticated, SAFE_METHODS


class IsAdminOrTaskOwner(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user == obj.created_by

class IsAdminOrReadOnly(IsAuthenticated):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user and request.user.is_staff

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsModeratorOrOwner(permissions.BasePermission):
    """
    разрешение, позволяющее модераторам редактировать любой фрагмент,
    но владельцы могут редактировать только свои фрагменты.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='Moderator').exists() or obj.owner == request.user
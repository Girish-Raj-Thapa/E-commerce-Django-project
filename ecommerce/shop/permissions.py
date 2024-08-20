from rest_framework import permissions 

class IsManager(permissions.BasePermission):
    """
    Custom permission to grant access only to users who belong to the 'Manager' group.
    """
    def has_permission(self, request, view):
        """
        Return `True` if the user belongs to the 'Manager' group, `False` otherwise.
        """
        return request.user.groups.filter(name="Manager").exists()

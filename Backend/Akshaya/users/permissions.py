from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user or not request.user.is_authenticated:
            return False
        # Check if the user has the required role
        return request.user.role in ['admin','super_admin']
    
# class IsStaff(permissions.BasePermission):
#     def has_permission(self, request, view):
#         # Check if the user is authenticated
#         if not request.user or not request.user.is_authenticated:
#             return False
#         # Check if the user has the required role
#         return request.user.role in ['staf','']
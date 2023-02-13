from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''Allow users to edit own profile'''

    def has_object_permission(self, request, view, obj):
        '''Check user is trying to edit own profile'''
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

        
class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return not request.user.is_authenticated
        return True
    
class IsAuthenticatedOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )
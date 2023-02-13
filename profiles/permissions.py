from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''Allow users to edit own profile'''

    def has_object_permission(self, request, view, obj):
        '''Check user is trying to edit own profile'''
        # return super().has_object_permission(request, view, obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

        
class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return not request.user.is_authenticated
        return request.user.is_authenticated
    

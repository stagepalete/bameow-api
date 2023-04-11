from rest_framework import permissions


class CheckOwnOrders(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)

# blog/permissions.py
from rest_framework import permissions
'''
    create custom permission 
    - check if the logged in user is the Auther of the post
    - inhert from permissions.BasePermission
    - update has_object_permission function to check my own permission
'''
class IsAutherOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.auther == request.user 
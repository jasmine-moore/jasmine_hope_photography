from rest_framework import permissions


class is_owner(permissions.BasePermission): 
    def has_object_permission(self, request, view, obj):  #runs function, returns true allows login, if false then no.  
        return obj.client_name == request.user

class isadminorreadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.username == "admin"


class readonly(permissions.BasePermission): 
    def has_permission(self, request, view):  
        if request.method in permissions.SAFE_METHODS:
            return True
        return False 


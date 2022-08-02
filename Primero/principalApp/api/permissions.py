from rest_framework import permissions
from principalApp.models import *

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        
        stuff_permission= bool(request.user and request.user.is_staff)
        #lo que se hace es modificar una funcion y preguntar si el usuario existe y si es un Staff
        return stuff_permission
class onlyUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request, view, obj):
        return obj.cliente==request.user
class onlyUsersTransactions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.cuentaB.cliente==request.user
class PermissionUser(permissions.IsAdminUser):
    def has_permission(self,request,view):
        if request.method=='GET':
            return True 
        return bool(request.user.is_staff)
        
    
    
    
        

        
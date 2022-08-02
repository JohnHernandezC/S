from django.shortcuts import get_object_or_404
from principalApp.models import Transaccion,TipoTransaccion, Cuenta
from .serializers import SerializerTipoTransaccion, SerializerCuenta ,serializerTransaccion
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from principalApp.api.permissions import AdminOrReadOnly,onlyUserOrReadOnly,onlyUsersTransactions,PermissionUser


class CuentaVS(viewsets.ViewSet):
    # def get_permissions(self):
    #     if self.action=='update':
    #         self.get
    #         permission_classes = [onlyUserOrReadOnly]
    #     elif self.action=='destroy':
            
    #         permission_classes = [onlyUserOrReadOnly]
    #     else:
            
    #         permission_classes = [IsAuthenticated]
            
    #     return [permission() for permission in permission_classes]
    
    def list(self, request):
        queryset=Cuenta.objects.all()
        serializer=SerializerCuenta(queryset, many=True)
        return Response (serializer.data)
    
    def create(self,request):
        serializer=SerializerCuenta(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def retrive(self, request, pk=None):
        queryset=Cuenta.objects.all()
        cuenta=get_object_or_404(queryset, pk=pk)
        serializer=SerializerCuenta(cuenta)
        return Response (serializer.data)
    
    
    def update(self, request, pk):
        
        try:
            queryset=Cuenta.objects.get(pk=pk)
        except Cuenta.DoesNotExist:
            return Response({'error','cuenta no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer=SerializerCuenta(queryset, data=request.data)
        #self.check_object_permissions(request, queryset)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request,pk):
        try: 
            queryset=Cuenta.objects.filter(pk=pk)
            p=Cuenta.objects.get(pk=pk)
        except Cuenta.DoesNotExist:
            return Response({'error','Cuenta no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        #self.check_object_permissions(request, p)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CuentaVSF(viewsets.ModelViewSet):
    queryset=Cuenta.objects.all()
    serializer_class=SerializerCuenta
        
#1////////////////////////////////////////////////////////////////////////        
        
class TipoTransaccionVS(viewsets.ViewSet):
    def get_permissions(self):
        permission_classes=[PermissionUser]
        return [permission() for permission in permission_classes]
    def list(self,request):
        queryset=TipoTransaccion.objects.all()
        serializer=SerializerTipoTransaccion(queryset, many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=SerializerTipoTransaccion(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    def retrive(self,request,pk=None):
        queryset=TipoTransaccion.objects.all()
        tipoT=get_object_or_404(queryset, pk=pk)
        serializer=SerializerTipoTransaccion(tipoT)
        return Response(serializer.data)
    def update(self,request,pk):
        try:
            queryset=TipoTransaccion.objects.get(pk=pk)
        except TipoTransaccion.DoesNotExist:
            return Response({'error','No se encontro este tipo de transaccion'}, status=status.HTTP_400_BAD_REQUEST)    
        #self.check_object_permissions(request,queryset)
        serializer=SerializerTipoTransaccion(request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk):
        try:
            queryset=TipoTransaccion.objects.filter(pk=pk)
            p=TipoTransaccion.objects.get(pk=pk)
        except TipoTransaccion.DoesNotExist:
            return Response ({'error','Tipo de Transaccion no encontrada'})
        #self.check_object_permissions(request,queryset)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
    #1////////////////////////////////////////////////////////////////////////  

class TransaccionVS(viewsets.ViewSet):
    
    def get_permissions(self):
        if self.action=='update' or self.action=='destroy':
            permission_classes=[onlyUsersTransactions]
        else:
            permission_classes=[IsAuthenticated]
        return (permission() for permission in permission_classes)
    
    permission_classes=[IsAuthenticated]
    
    def list(self,request):
        queryset=Transaccion.objects.all()
        print(queryset) 
        serializer=serializerTransaccion(queryset, many=True)
        return Response(serializer.data)
    def create (self, request):
        serializer=serializerTransaccion(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
    def retrive(self, request, pk=None):
        queryset=Transaccion.objects.all()
        transaccion=get_object_or_404(queryset, pk=pk)
        serializer=serializerTransaccion(transaccion)
        return Response( serializer.data)
    def update (self, request, pk):
        try:
            queryset=Transaccion.objects.get(pk=pk)
        except Transaccion.DoesNotExist:
            return Response ({'error','Transaccion no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request, queryset)
        serializer=serializerTransaccion(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        try:
            queryset=Transaccion.objects.filter(pk=pk)
            p=Transaccion.objects.get(pk=pk)
        except Transaccion.DoesNotExist:
            return Response({'error','objeto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(request,p)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class TransaccionVSF (viewsets.ModelViewSet):
    queryset=Transaccion.objects.all()
    serializer_class=serializerTransaccion

              
            
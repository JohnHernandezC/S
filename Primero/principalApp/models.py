from tkinter import CASCADE
from django.db import models
from userApp.models import Usuarios

# Create your models here

class Cuenta (models.Model):
    moneda=models.CharField(max_length=20)
    cliente=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.moneda
    
class TipoTransaccion(models.Model):
    tipo=models.CharField(max_length=20)
    descripcion=models.TextField()
    def __str__(self):
        return self.tipo
    
class Transaccion (models.Model):
    cuentaB=models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    tipoT=models.ForeignKey(TipoTransaccion, on_delete=models.CASCADE)
    monto=models.FloatField()
    
    def __str__(self):
        return str(self.cuentaB) 
    
        

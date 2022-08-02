
from rest_framework import serializers
from principalApp.models import Transaccion,TipoTransaccion, Cuenta

class SerializerCuenta (serializers.ModelSerializer):
    cliente=serializers.StringRelatedField(read_only=True)
    #monedale=serializers.SerializerMethodField()
    class Meta:
        model=Cuenta
        fields='__all__'
        
    # def get_monedale(self,object):
    #     caracteres=len(object.moneda)
    #     return caracteres
class SerializerTipoTransaccion(serializers.ModelSerializer):
    class Meta:
        model=TipoTransaccion
        fields='__all__'
        
class serializerTransaccion(serializers.ModelSerializer):
    class Meta:
        model=Transaccion
        fields='__all__'
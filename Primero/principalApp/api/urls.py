from django.urls import path,include
from rest_framework.routers import DefaultRouter
from principalApp.api.views import CuentaVS,TipoTransaccionVS, TransaccionVS

router=DefaultRouter()
router.register(r'cuentas', CuentaVS, basename='cuentas')
router.register(r'Tipotransaccion', TipoTransaccionVS, basename='TipoTransaccion')
router.register(r'transaccion', TransaccionVS, basename='Transaccion')
urlpatterns = router.urls
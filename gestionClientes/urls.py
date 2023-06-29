from django.urls import include, path
from rest_framework import routers
from .views import PedidoViewSet,ProductoViewSet,ClienteViewSet , UsuariosViewSet

router = routers.DefaultRouter()
router.register('pedidos', PedidoViewSet, )
router.register ('productos', ProductoViewSet) 
router.register ('clientes', ClienteViewSet)
router.register ('usuarios', UsuariosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

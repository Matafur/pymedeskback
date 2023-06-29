from rest_framework import viewsets
from .models import Pedido,cliente,Producto, usuarios
from .serializers import PedidoSerializer, ClienteSerializer, ProductoSerializer, UsuariosSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ClienteViewSet (viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer

class ProductoViewSet (viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class UsuariosViewSet (viewsets.ModelViewSet):
    queryset = usuarios.objects.all()
    serializer_class = UsuariosSerializer
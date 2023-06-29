from rest_framework import serializers
from .models import Producto, Pedido, cliente, usuarios

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion']

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = ['idPedido', 'fechaPedido', 'estadoPedido', 'pagoPedido', 'reglaEnvio','observaciones']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ['id', 'nombreCliente','emailCliente','direccionCliente','ciudadCliente' ]

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuarios
        fields = ['id', 'nombreUsuario','emailUsuario','emailPassword' ]
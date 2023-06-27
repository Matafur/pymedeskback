from django.db import models

class Producto(models.Model):
    
    id = models.AutoField(primary_key=True, editable=False)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=400, default='Valor predeterminado')


class Pedido(models.Model):

    estado_Pedido = [
    ('pendiente', 'Pendiente'),
    ('en_ruta', 'En ruta'),
    ('entregado', 'Entregado'),
    ('cancelado', 'Cancelado'),
    
    ]
    regla_Envio =[
    ('domicilio', 'Domicilio'),
    ('punto de Venta', 'Punto de Venta'),
    ]

    idPedido= models.AutoField(primary_key=True, editable=False)
    fechaPedido = models.DateField()
    estadoPedido = models.CharField(max_length=20, choices=estado_Pedido)
    pagoPedido = models.BooleanField(default=False)  
    reglaEnvio = models.CharField(max_length=20, choices=regla_Envio )
    observaciones = models.CharField(max_length=100)

class cliente(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nombreCliente = models.CharField(max_length=100)
    emailCliente = models.EmailField(max_length=100)
    direccionCliente = models.CharField(max_length=100)
    ciudadCliente = models.CharField(max_length=100)
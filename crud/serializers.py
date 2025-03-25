from rest_framework import serializers
from .models import Cliente, Producto, Pedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'email', 'telefono', 'activo']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'stock', 'categoria']

class PedidoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(), 
        source='cliente', 
        write_only=True
    )

    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'cliente_id', 'fecha', 'total', 'estado']
        read_only_fields = ['fecha']
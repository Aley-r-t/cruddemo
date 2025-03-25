from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cliente, Producto, Pedido
from .serializers import ClienteSerializer, ProductoSerializer, PedidoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    @action(detail=False, methods=['GET'])
    def activos(self, request):
        """Obtener solo clientes activos"""
        clientes_activos = self.queryset.filter(activo=True)
        serializer = self.get_serializer(clientes_activos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def cambiar_estado(self, request, pk=None):
        """Cambiar estado de activación del cliente"""
        cliente = self.get_object()
        cliente.activo = not cliente.activo
        cliente.save()
        serializer = self.get_serializer(cliente)
        return Response(serializer.data)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    @action(detail=False, methods=['GET'])
    def por_categoria(self, request):
        """Filtrar productos por categoría"""
        categoria = request.query_params.get('categoria', None)
        if categoria:
            productos = self.queryset.filter(categoria=categoria)
            serializer = self.get_serializer(productos, many=True)
            return Response(serializer.data)
        return Response({"error": "Categoría no proporcionada"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['PATCH'])
    def actualizar_stock(self, request, pk=None):
        """Actualizar stock de un producto"""
        producto = self.get_object()
        nuevo_stock = request.data.get('stock')
        
        if nuevo_stock is not None:
            producto.stock = nuevo_stock
            producto.save()
            serializer = self.get_serializer(producto)
            return Response(serializer.data)
        return Response({"error": "Stock no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    @action(detail=False, methods=['GET'])
    def por_estado(self, request):
        """Filtrar pedidos por estado"""
        estado = request.query_params.get('estado', None)
        if estado:
            pedidos = self.queryset.filter(estado=estado)
            serializer = self.get_serializer(pedidos, many=True)
            return Response(serializer.data)
        return Response({"error": "Estado no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['PATCH'])
    def cambiar_estado(self, request, pk=None):
        """Cambiar estado del pedido"""
        pedido = self.get_object()
        nuevo_estado = request.data.get('estado')
        
        if nuevo_estado:
            pedido.estado = nuevo_estado
            pedido.save()
            serializer = self.get_serializer(pedido)
            return Response(serializer.data)
        return Response({"error": "Estado no proporcionado"}, status=status.HTTP_400_BAD_REQUEST)
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ClienteViewSet, ProductoViewSet, PedidoViewSet

# Crear un router para manejar las rutas de ViewSets
router = DefaultRouter()

# Registrar los ViewSets en el router
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'pedidos', PedidoViewSet, basename='pedido')

urlpatterns = [
    # Incluir las rutas generadas por el router
    path('api/', include(router.urls)),

    # Rutas personalizadas adicionales (opcional)
    path('api/clientes/activos/', ClienteViewSet.as_view({'get': 'activos'}), name='clientes-activos'),
    path('api/productos/por-categoria/', ProductoViewSet.as_view({'get': 'por_categoria'}), name='productos-por-categoria'),
    path('api/pedidos/por-estado/', PedidoViewSet.as_view({'get': 'por_estado'}), name='pedidos-por-estado'),
]
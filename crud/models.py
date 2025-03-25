from django.db import models

# Create your models here.


from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'activo': self.activo
        }

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': float(self.precio),
            'stock': self.stock,
            'categoria': self.categoria
        }

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20)

    def to_dict(self):
        return {
            'id': self.id,
            'cliente_id': self.cliente.id,
            'cliente_nombre': self.cliente.nombre,
            'fecha': self.fecha.isoformat(),
            'total': float(self.total),
            'estado': self.estado
        }
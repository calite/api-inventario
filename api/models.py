from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import User

# Modelo de Usuario con roles específicos
# class User(AbstractUser):
#     ROLE_CHOICES = (
#         ('admin', 'Administrador'),
#         ('employee', 'Empleado'),
#         ('client', 'Cliente'),
#     )
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
#     groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
#     user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set', blank=True)

# Modelo para los tipos de productos
class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Modelo para los productos
class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    qr_code = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

# Modelo para los accesorios
class Accessory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    qr_code = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

# Modelo para la agenda y las reservas
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    accessories = models.ManyToManyField(Accessory, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} - {self.start_date} to {self.end_date}'

# Modelo para el checkout
class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    accessories = models.ManyToManyField(Accessory, blank=True)
    checkout_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.checkout_date}'

# Modelo para la gestión de incidencias
class Incident(models.Model):
    INCIDENT_TYPE_CHOICES = (
        ('lost', 'Perdido'),
        ('damaged', 'Dañado'),
        ('other', 'Otro'),
    )
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    accessory = models.ForeignKey(Accessory, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    incident_type = models.CharField(max_length=10, choices=INCIDENT_TYPE_CHOICES)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.incident_type} reported by {self.reported_by.username}'

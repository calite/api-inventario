from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, ProductType, Product, Accessory, Reservation, Checkout, Incident
from .serializer import (
    UserSerializer, ProductTypeSerializer, ProductSerializer,
    AccessorySerializer, ReservationSerializer, CheckoutSerializer,
    IncidentSerializer
)

# Vistas para el modelo User
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# Vistas para el modelo ProductType
class ProductTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

# Vistas para el modelo Product
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

# Vistas para el modelo Accessory
class AccessoryList(generics.ListCreateAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = [permissions.IsAuthenticated]

class AccessoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = [permissions.IsAuthenticated]

# Vistas para el modelo Reservation
class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

# Vistas para el modelo Checkout
class CheckoutList(generics.ListCreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = [permissions.IsAuthenticated]

class CheckoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    permission_classes = [permissions.IsAuthenticated]

# Vistas para el modelo Incident
class IncidentList(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

class IncidentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]

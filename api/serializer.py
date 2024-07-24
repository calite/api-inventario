from rest_framework import serializers
from .models import User, ProductType, Product, Accessory, Reservation, Checkout, Incident

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role']

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer(read_only=True)
    product_type_id = serializers.PrimaryKeyRelatedField(queryset=ProductType.objects.all(), source='product_type')

    class Meta:
        model = Product
        fields = ['id', 'product_type', 'product_type_id', 'name', 'description', 'qr_code']

class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = ['id', 'name', 'description', 'qr_code']

class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    products = ProductSerializer(many=True, read_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, source='products')
    accessories = AccessorySerializer(many=True, read_only=True)
    accessory_ids = serializers.PrimaryKeyRelatedField(queryset=Accessory.objects.all(), many=True, source='accessories', required=False)

    class Meta:
        model = Reservation
        fields = ['id', 'user', 'user_id', 'products', 'product_ids', 'accessories', 'accessory_ids', 'start_date', 'end_date']

class CheckoutSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    products = ProductSerializer(many=True, read_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True, source='products')
    accessories = AccessorySerializer(many=True, read_only=True)
    accessory_ids = serializers.PrimaryKeyRelatedField(queryset=Accessory.objects.all(), many=True, source='accessories', required=False)

    class Meta:
        model = Checkout
        fields = ['id', 'user', 'user_id', 'products', 'product_ids', 'accessories', 'accessory_ids', 'checkout_date']

class IncidentSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, required=False)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', allow_null=True)
    accessory = AccessorySerializer(read_only=True, required=False)
    accessory_id = serializers.PrimaryKeyRelatedField(queryset=Accessory.objects.all(), source='accessory', allow_null=True)
    reported_by = UserSerializer(read_only=True)
    reported_by_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='reported_by')

    class Meta:
        model = Incident
        fields = ['id', 'product', 'product_id', 'accessory', 'accessory_id', 'description', 'incident_type', 'reported_by', 'reported_by_id', 'reported_at']

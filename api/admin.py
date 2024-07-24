from django.contrib import admin
from .models import User, ProductType, Product, Accessory, Reservation, Checkout, Incident

# Register your models here.

admin.site.register(User)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Accessory)
admin.site.register(Reservation)
admin.site.register(Checkout)
admin.site.register(Incident)
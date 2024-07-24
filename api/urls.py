from django.urls import path, include
from rest_framework import routers
from .views import (
    UserList, UserDetail, ProductTypeList, ProductTypeDetail,
    ProductList, ProductDetail, AccessoryList, AccessoryDetail,
    ReservationList, ReservationDetail, CheckoutList, CheckoutDetail,
    IncidentList, IncidentDetail
)

router = routers.DefaultRouter()

urlpatterns = [
    path('',include(router.urls)),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('product-types/', ProductTypeList.as_view(), name='producttype-list'),
    path('product-types/<int:pk>/', ProductTypeDetail.as_view(), name='producttype-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('accessories/', AccessoryList.as_view(), name='accessory-list'),
    path('accessories/<int:pk>/', AccessoryDetail.as_view(), name='accessory-detail'),
    path('reservations/', ReservationList.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', ReservationDetail.as_view(), name='reservation-detail'),
    path('checkouts/', CheckoutList.as_view(), name='checkout-list'),
    path('checkouts/<int:pk>/', CheckoutDetail.as_view(), name='checkout-detail'),
    path('incidents/', IncidentList.as_view(), name='incident-list'),
    path('incidents/<int:pk>/', IncidentDetail.as_view(), name='incident-detail'),
]

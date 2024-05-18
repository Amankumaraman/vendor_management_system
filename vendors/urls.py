from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import VendorViewSet, PurchaseOrderViewSet, RegisterView

urlpatterns = [
    path('token/', obtain_auth_token, name='api_token_auth'),  # Token authentication endpoint
    path('vendors/', VendorViewSet.as_view({'get': 'list', 'post': 'create'}), name='vendor-list'),
    path('vendors/<int:pk>/', VendorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='vendor-detail'),
    path('purchase_orders/', PurchaseOrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='purchase-order-list'),
    path('purchase_orders/<int:pk>/', PurchaseOrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='purchase-order-detail'),
    path('register/generic/', RegisterView.as_view(), name='register_generic'),
]

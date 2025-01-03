from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view(), name='register_user'),
    path('token/', views.ObtainTokenView.as_view(), name='obtain_token'),
    path('token/refresh/', views.RefreshTokenView.as_view(), name='refresh_token'),
    path('products/', views.ListProductsView.as_view(), name='list_products'),
    path('vendor/products/', views.VendorProductsView.as_view(), name='vendor_products'),
    path('vendor/products/add/', views.AddProductView.as_view(), name='add_product'),
    path('orders/', views.PlaceOrderView.as_view(), name='place_order'),
    path('payment/', views.InitiatePaymentView.as_view(), name='initiate_payment'),
    path('admin/users/', views.ListUsersView.as_view(), name='list_users'),
    path('admin/approve-vendor/', views.ApproveVendorView.as_view(), name='approve_vendor'),
]

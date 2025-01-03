from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user),
    path('token/', views.obtain_token),
    path('products/', views.ProductListView.as_view()),
    path('vendor/products/', views.VendorProductView.as_view()),
]

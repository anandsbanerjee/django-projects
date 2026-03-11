from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.get_products, name='prodcuts'),
    path('products/<int:sku>/', views.get_prodcut_detail, name='prodcut_detail'),
]
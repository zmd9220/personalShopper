from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.products),
    path('product/<int:product_id>/', views.product_detail),
    path('product/<int:product_id>/stocks/', views.product_stock),
]

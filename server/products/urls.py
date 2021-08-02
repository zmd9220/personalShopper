from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.product_index),
    path('product/<int:product_id>/', views.product_detail),
]

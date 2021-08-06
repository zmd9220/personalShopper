from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.products), # 전체 상품조회
    path('product/<int:product_id>/', views.product_detail), # 특정 상품 조회
    path('product/<int:product_id>/stocks/', views.product_stock), # 특정 상품 재고 조회
]

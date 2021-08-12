from django.urls import path
from . import views


app_name = 'products'

urlpatterns = [
    path('products/', views.products), # 전체 상품조회
    path('product/<int:product_id>/', views.product_detail), # 특정 상품 조회
    path('product/<int:product_id>/stocks/', views.product_stock), # 특정 상품 재고 조회
    path('kakaoPay/', views.kakaoPay), # 카카오페이 결제
    path('recommended/', views.recommended), # 추천
    
    path('product/create/', views.product_list_create),
    path('product/<int:product_pk>/update/', views.product_update_delete),
]


# GET: /api/products/  # 상품 전체 리스트 조회
# POST: /api/products # 상품 추가
# DELETE: /api/products/{product_id}/ # 상품 삭제
# GET: /api/products/{product_id}/ # 특정 상품 조회
# PUT: /api/products/{product_id}/ # 특정 상품 정보 수정

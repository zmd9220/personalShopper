from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, StockSerializer
from .models import Product, Stock


@api_view(['GET'])       # 전체 상품 조회
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)


@api_view(['GET'])                  # 특정 상품 조회
def product_detail(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product, product_id = product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(['GET'])                # 특정 상품 재고 조회
def product_stock(request, product_id):
    if request.method == 'GET':
        stocks = get_object_or_404(Stock, product_id = product_id)
        serializers = StockSerializer(stocks)
        return Response(serializers.data)

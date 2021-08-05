from django.shortcuts import get_object_or_404, render
from django.views.decorators import csrf
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from rest_framework.decorators import authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import ProductSerializer, CustomerSerializer, StockSerializer
from .models import Product, Customer, Stock

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import ProductForm


@api_view(['GET'])
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def product_detail(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Product, product_id = product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(['GET'])
def product_stock(request, product_id):
    if request.method == 'GET':
        stocks = get_object_or_404(Stock, product_id = product_id)
        serializers = StockSerializer(stocks)
        return Response(serializers.data)

# 저장 된 모든 할 일 데이터를 불러온 후에 하나씩 json 데이터로 가공할 수 있게 사전형 데이터로 저장
# 마지막으로 JsonResponse 형태로 데이터를 반환하면 Vue.js앱에서 데이터를 받아서 보여주게된다.
# def product_fetch(request):
#     products = Product.objects.all()
#     product_list = []
#     for product in products:
#         product_list.append({'product_id': product.product_id, 'name': product.product_name })
#     return JsonResponse(product_list, safe=False)

# @csrf_exempt
# def product_save(request): # product 목록을 전체 데이터로 받아 그대로 저장
#     if request.body:
#         data = json.loads(request.body)
#         if 'products' in data: # 그런데 뷰를 호출 할 때 마다 데이터 확인 없이 데이터를 지우게되면 문제가 발생함으로 확인
#             products = data['products']
#             Product.objects.all().delete() #2 전체 데이터를 지우고 다시 입력하는 방식 사용
#         for product in products:
#             print('product', product)
#             form = ProductForm(product) # 데이터를 저장
#             if form.is_valid():
#                 form.save() # DB에 저장
#     return JsonResponse({})
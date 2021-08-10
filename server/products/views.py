import os
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, StockSerializer
from .models import Product, Stock
import json, requests


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

    
@api_view(['POST'])     # 카카오페이 결제 
def kakaoPay(request):
    url = "https://kapi.kakao.com"
    headers = {
        'Authorization': "KakaoAK " + "4595b53acfdd636260c962e7fd4c8dd0", # admin key 처리 해야함
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    params = {
        'cid': "TC0ONETIME",
        'partner_order_id': '1001',
        'partner_user_id': 'ssafy',
        'item_name': '포인트',
        'quantity': 1,
        'total_amount': 201, # 'total_amount' >  'vat_amount'
        'vat_amount': 200,
        'tax_free_amount': 0,
        'approval_url': 'http://localhost:8080',
        'fail_url': 'http://localhost:8080',
        'cancel_url': 'http://localhost:8080',
    }
    response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
    response = json.loads(response.text)
    return Response(response)

@api_view(['GET'])
def make_status(request):
    module_dir = os.path.abspath('../embedded/status')
    print(os.path.abspath('../embedded/status'))
    file_path = os.path.join(module_dir, 'barcode.txt')
    with open(file_path, 'a+', encoding='utf-8') as txtfile:
        tmp_str = '생성 완료'
        txtfile.write(tmp_str)
    print(file_path)
    # os.remove(file_path)
    if os.path.isfile(file_path): 
        return Response(status=200)
    else:
        return Response(status=404)
  
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

    
@api_view(['POST'])     # 카카오페이 결제 준비
def kakaoPay_ready(request):
    url = "https://kapi.kakao.com"
    headers = {
        'Authorization': "KakaoAK " + "4595b53acfdd636260c962e7fd4c8dd0", # admin key 처리 해야함
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    # print(request.data)
    # print(request)
    params = {
        'cid': "TC0ONETIME",
        'partner_order_id': request.data['orderNumber'],
        'partner_user_id': 'ssafy',
        # 상품 이름
        'item_name': request.data['product_name'],
        # 갯수
        'quantity': 1,
        # 총 가격
        'total_amount': request.data['price'], # 'total_amount' >  'vat_amount'
        # 부가세 국내에선 포함 가격일 듯
        'vat_amount': 0,
        # 면세
        'tax_free_amount': 0,
        # 성공시 반환할 url
        'approval_url': 'http://localhost:8080/isApprove',
        # 실패시 반환할 url
        'fail_url': 'http://localhost:8080/isApprove',
        # 취소시 반환할 url
        'cancel_url': 'http://localhost:8080/isApprove',
    }
    response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
    response = json.loads(response.text)
    print(response)
    return Response(response)

@api_view(['POST'])     # 카카오페이 결제 승인 요청 
def kakaoPay_approve(request):
    url = "https://kapi.kakao.com"
    headers = {
        'Authorization': "KakaoAK " + "4595b53acfdd636260c962e7fd4c8dd0", # admin key 처리 해야함
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    # print(request.data)
    # print(request)
    params = {
        # 가맹점 코드
        'cid': "TC0ONETIME",
        # 결제 고유 번호
        'tid': request.data['tid'],
        # 가맹점 주문 번호
        'partner_order_id': request.data['orderNumber'],
        # 가맹점 회원 id
        'partner_user_id': 'ssafy',
        # 결제 승인을 요청하는 토큰
        'pg_token': request.data['pg_token'],
    }
    response = requests.post(url+"/v1/payment/approve", params=params, headers=headers)
    response = json.loads(response.text)
    print(response)
    return Response(response)

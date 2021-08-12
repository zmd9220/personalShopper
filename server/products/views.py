from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, StockSerializer
from .models import Product, Stock, Recommend
import json, requests

from rest_framework import status

from rest_framework.decorators import authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

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


@api_view(['POST']) # 추천 알고리즘
def recommended(request):
    age = request.POST.get('age')
    gen = request.POST.get('gen')
    
    if int(age) < 20:
        recommend_age = Recommend.objects.all().order_by('-week_sale10','-month_sale10','-visit10')
    elif 20 <= int(age) < 30:
        recommend_age = Recommend.objects.all().order_by('-week_sale20','-month_sale20','-visit20')
    elif 30 <= int(age) < 40:
        recommend_age = Recommend.objects.all().order_by('-week_sale30','-month_sale30','-visit30')
    elif 40 <= int(age) < 50:
        recommend_age = Recommend.objects.all().order_by('-week_sale40','-month_sale40','-visit40')
    elif 50 <= int(age) < 60:
       recommend_age = Recommend.objects.all().order_by('-week_sale50','-month_sale50','-visit50')
    else :
        recommend_age = Recommend.objects.all().order_by('-week_sale60','-month_sale60','-visit60')

    products_gen = Product.objects.filter(gender=gen)    
    result = []
    for i in recommend_age:
        for j in products_gen:
            if i.product_id == j.product_id:
                result.append(str(j.product_id))
    recommend_data = {
        "A": result[0],
        "B": result[1],
        "C": result[2],
        "D": result[3],
    }
    response = json.dumps(recommend_data)
    return Response(response)


@api_view(['GET', 'POST'])
# JWT 을 활용한 인증을 할 때 JWT 자체를 검증한 인증 여부와 상관 없이 JWT가 유효한 지 여부만 파악
# @authentication_classes([JSONWebTokenAuthentication])
# # 인증이 되지 않은 상태로 요청이 없으면
# # "자격 인증 데이터가 제공되지 않았습니다"와 같은 메세지를 응답함
# @permission_classes([IsAuthenticated])
def product_list_create(request):
    if request.method == 'GET':
        # products = product.objects.all()
        serializer = ProductSerializer(request.user.products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def product_update_delete(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    # 1. 해당 product의 유저가 아닌 경우 product를 수정하거나 삭제하지 못하게 설정
    # if not request.user.products.filter(pk=product_pk).exists():
    #     return Response({ 'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        product.delete()
        return Response({ 'id': product_pk }, status=status.HTTP_204_NO_CONTENT)
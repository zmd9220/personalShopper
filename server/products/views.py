import os
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

ages = ['10', '20', '30', '40', '50', '60']
# sizes = []

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

@api_view(['GET'])
def make_status(request):
    # /server 에서 장고를 실행했을 때, 정상적으로 돌아감.. 안그러면 문제가 발생
    module_dir = os.path.abspath('../embedded/status')
    # module_dir까지의 경로/barcode.txt 로 경로 문자열 생성
    file_path = os.path.join(module_dir, 'barcode.txt')
    # txt 파일 생성 후 저장
    with open(file_path, 'a+', encoding='utf-8') as txtfile:
        tmp_str = '생성 완료'
        txtfile.write(tmp_str)
    # os.remove(file_path)
    # 현재 파일 경로에 잘 생성 되었으면 200 아니면 404
    if os.path.isfile(file_path): 
        return Response(status=200)
    else:
        return Response(status=404)
  
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
    if response.status_code == 200:
        print(request.data)
        user_data = request.data['userData']
        order_items = request.data['orderItems']
        for item in order_items:
            stock = get_object_or_404(Stock, product_id=item['product_id'])
            sales = get_object_or_404(Recommend, product_id=item['product_id'])
            if user_data['age'] in ages:
                age = user_data['age']
                if age == 10:
                    sales.week_sale10 += 1
                    sales.month_sale10 += 1
                elif age == 20:
                    sales.week_sale20 += 1
                    sales.month_sale20 += 1
                elif age == 30:
                    sales.week_sale30 += 1
                    sales.month_sale30 += 1
                elif age == 40:
                    sales.week_sale40 += 1
                    sales.month_sale40 += 1
                elif age == 50:
                    sales.week_sale50 += 1
                    sales.month_sale50 += 1
                else:
                    sales.week_sale60 += 1
                    sales.month_sale60 += 1
            sales.save()
        print(user_data)
        print(order_items)
        
    response_data = json.loads(response.text)
    response_data['status_code'] = response.status_code
    # print(response_data)
    return Response(response_data)


@api_view(['POST']) # 추천 알고리즘
def recommended(request):
    age = request.POST.get('age')  # veu에서 나이 데이터 불러오기
    gen = request.POST.get('gen') # veu에서 성별 데이터 불러오기
    
    if int(age) < 20:
        recommend_age = Recommend.objects.all().order_by('-week_sale10','-month_sale10','-visit10')  # 받은 데이터의 나이를 기준으로 나이에 대한 주간, 원간, 방문 데이터 내림차순 정렬
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

    products_gen = Product.objects.filter(gender=gen)   # 해당되는 성별만 필터링
    result = []

    for i in recommend_age:         # 필터링한 성별과 내림차순 한 데이터에서 교집합 되는 부분 찾기
        for j in products_gen:
            if i.product_id == j.product_id:
                result.append([str(j.product_id),str(j.style_image)]) # 상품 아이디 값과 스타일 이미지 값 저장

    res = [] # 최종 상품 아이디가 담길 변수
    style = [] # 중복 스타일 추천 방지를 위한 변수 
    res.append(result[0][0])
    style.append(result[0][1])


    for i in range(1,len(result)):
        if len(res) == 4:
            break
        if result[i][1] not in style: # 중복 스타일 추천 방지를 위한 코드
            res.append(result[i][0])
            style.append(result[i][1])
        

    recommend_data = {  # 추천 알고리즘 사용하여 선별된 상위 4개 항목 vue로 전달
        "A": res[0],
        "B": res[1],
        "C": res[2],
        "D": res[3],
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

import os
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, StockSerializer
from .models import Product, Stock, Recommend
import json, requests

from rest_framework import status


# stock 테이블에 사이즈 접근을 위한 dictionary
sizes = {
    'M1': ['XS (KR 90)', 'S (KR 95)', 'M (KR 95-100)', 'L (KR 100-105)', 'XL (KR 105-110)'],
    'F1': ['XS (KR 44)', 'S (KR 55)', 'M (KR 66)', 'L (KR 77)', 'XL (KR 88)'],
    'M2': ['XS (KR 28)', 'S (KR 30)', 'M (KR 31)', 'L (KR 32)', 'XL (KR 34)'],
    'F2': ['XS (KR 24)', 'S (KR 26)', 'M (KR 28)', 'L (KR 30)', 'XL (KR 32)'],
    'M3': ['KR 250', 'KR 260', 'KR 270', 'KR 280', 'KR 290'],
    'F3': ['KR 230', 'KR 240', 'KR 250', 'KR 260', 'KR 270'],
}

@api_view(['GET'])       # 전체 상품 조회
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)


@api_view(['GET', 'POST'])                  # 특정 상품 조회
def product_detail(request, product_id):
    # GET - 데이터 조회만
    # 조회할 상품 데이터 가져오기
    product = get_object_or_404(Product, product_id = product_id)
    # POST - 데이터 조회 및 recommend 테이블의 visit'연령' 컬럼에 +1
    if request.method == 'POST':
        # visit를 수정할 해당 상품 recommend 테이블의 row 가져오기
        visit = get_object_or_404(Recommend, product_id = product_id)
        age = int(request.data['age'])
        # 나이 대에 맞추어 변경
        if age < 20:
            visit.visit10 += 1
        elif age < 30:
            visit.visit20 += 1
        elif age < 40:
            visit.visit30 += 1
        elif age < 50:
            visit.visit40 += 1
        elif age < 60:
            visit.visit50 += 1
        else:
            visit.visit60 += 1
        # 변경 내역 저장
        visit.save()        
    # 직렬화를 통해 json화
    serializer = ProductSerializer(product)
    # 데이터 클라이언트로 전달
    return Response(serializer.data)


@api_view(['GET'])                # 특정 상품 재고 조회
def product_stock(request, product_id):
    if request.method == 'GET':
        stocks = get_object_or_404(Stock, product_id = product_id)
        serializers = StockSerializer(stocks)
        return Response(serializers.data)

    
@api_view(['POST'])     # 카카오페이 결제 준비
def kakaoPay_ready(request):
    # 카카오 페이 api url
    url = "https://kapi.kakao.com"
    # 헤더 - api key와 타입 지정
    headers = {
        'Authorization': "KakaoAK " + "4595b53acfdd636260c962e7fd4c8dd0", # admin key 처리 해야함
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    # 요청에 필요한 파라미터 값 지정
    params = {
        # 가맹점 코드
        'cid': "TC0ONETIME",
        # 상품 결제 번호(우리 측) - 고유 번호
        'partner_order_id': request.data['orderNumber'],
        # 상품 회원 id 
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
    # 요청 보냄
    response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
    # 응답 받기 - 카카오 페이 측에서 이상이 없는 이상 200으로 올 것
    # 받은 데이터를 json으로 변경 후 클라이언트로 전달
    response = json.loads(response.text)
    return Response(response)


@api_view(['GET'])
def make_status(request):
    # /server 에서 장고를 실행했을 때, 정상적으로 돌아감.. 안그러면 문제가 발생
    module_dir = os.path.abspath('../embedded/status')
    # module_dir까지의 경로/barcode.txt 로 경로 문자열 생성
    file_path = os.path.join(module_dir, 'barcode.txt')
    # txt 파일 생성 후 저장
    with open(file_path, 'w', encoding='utf-8') as txtfile:
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
    # 카카오 페이 api url
    url = "https://kapi.kakao.com"
    # 헤더 - api key와 타입 지정
    headers = {
        'Authorization': "KakaoAK " + "4595b53acfdd636260c962e7fd4c8dd0", # admin key 처리 해야함
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    # 요청에 필요한 파라미터 값 지정
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
    # 요청 보냄
    response = requests.post(url+"/v1/payment/approve", params=params, headers=headers)
    # 응답 코드가 200 = 정상적으로 승인이 완료 되었음 -> DB에 재고 -1, 판매 +1
    if response.status_code == 200:
        # 현재 키오스크를 보고 있는 유저 정보
        user_data = request.data['userData']
        # 현재 구매한 장바구니 상품들
        order_items = request.data['orderItems']
        # 각 상품 별로 DB에 반영

        for item in order_items:
            # recommend 테이블에 해당 상품 row
            sales = get_object_or_404(Recommend, product_id=item['product_id'])
            age = int(user_data['age'])
            # 유저의 나이대에 맞추어 해당 제품 판매량 갱신
            if age < 20:
                sales.week_sale10 += 1
                sales.month_sale10 += 1
            elif age < 30:
                sales.week_sale20 += 1
                sales.month_sale20 += 1
            elif age < 40:
                sales.week_sale30 += 1
                sales.month_sale30 += 1
            elif age < 50:
                sales.week_sale40 += 1
                sales.month_sale40 += 1
            elif age < 60:
                sales.week_sale50 += 1
                sales.month_sale50 += 1
            else:
                sales.week_sale60 += 1
                sales.month_sale60 += 1
            # stock 테이블에 해당 상품 row
            stock = get_object_or_404(Stock, product_id=item['product_id'])
            # sizes 딕셔너리를 접근하기 위한 키값 생성 - 'M1, F1, M2, F2, M3, F3, M4, F4' 중 하나 생성됨
            product_type = item['gender']+str(item['product_type'])
            # M4, F4를 제외하면 경우는 모두 사이즈가 별도로 있으므로 접근하여 -1
            if product_type in sizes:
                stock.stock[sizes[product_type].index(item['selectedSize'])] -= 1
            else: # 악세서리(M4, F4) 인 경우 프리 스타일이므로 0번 인덱스로 접근
                stock.stock[0] -= 1
            # DB에 실제 저장
            sales.save()
            stock.save()
    # 응답 받은 데이터를 json화
    response_data = json.loads(response.text)
    # 클라이언트에서 상태 코드를 기반으로 분기를 나누기 때문에 상태 코드를 추가
    response_data['status_code'] = response.status_code
    # 클라이언트에 전달
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
# # 인증이 되지 않은 상태로 요청이 없으면
# # "자격 인증 데이터가 제공되지 않았습니다"와 같은 메세지를 응답함
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

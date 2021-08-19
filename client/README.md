# 환경설정

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```



## 컴포넌트 구조



* App
  * Main
  * Ad
    * Adclient
  * Barcode
    * Nav
    * FooterAdBarcode
  * PersonalShopper
    * PersonalShopperDetail
  * ProductDetail
    * Nav
    * FooterAd
    * ProductDetailLocation
    * ProductSizeRecommand
  * Cart
    * CartList
  * Payment
    * isApprove
    * OrderComplete
  * Account
    * Login
    * Signup
  * Admin
    * Admin
    * ProductForm

# Frontend

* vue, vuex, bootstrap-vue 사용하여 구성.
* 사용자를 위한 키오스크 용도의 페이지와
* 매장 관리자를 위한 관리 페이지가 존재.



## Kiosk page

* Ad 

  * 광고를 위한 페이지. 초음파 센서에 의해 사용자가 인식되지않으면 표시되는 페이지.
* Main

  * 바코드로 상품을 조회하는 페이지와 상품추천 서비스를 받을수 있는 퍼스널쇼퍼 페이지로의 이동을 담당.
  * Vue 라이프사이클의 created에 인식된 개인정보(나이,성별)을 바탕으로 추천상품의 초기값을 받아둔다.
* Barcode

  * 바코드로 상품 상세정보를 얻기 위한 페이지
  * 하단의 FooterAd가 존재하며 추천알고리즘에 의한 3가지 아이템이 추천된다.
* PersonalShopper

  * 추천시스템에 의해 4개의 모델사진이 보여지는 페이지.
  * 모델사진을 클릭하면 PersonalShopperDetail 페이지로 이동.
    * 모델이 착용한 다른아이템을 footer형태로 보여주고 클릭시 이동.
    * 룩 세트로 구매 버튼 클릭시 (모든아이템 장바구니 추가 + 장바구니 이동.)
* ProductDetail

  * 제품 상세페이지.

  * 제품에 대한 상세정보(이름, 사진, 재고정보)를 보여주고 선택항목으로

    * 바로구매(장바구니 저장 + 장바구니 이동)

    * 카트추가(장바구니 저장)
    * 사이즈 추천받기
      * 개인정보(키, 몸무게)를 입력하여 대략적인 사이즈를 결정하는 데 도움을 준다. 
    * 상품위치 등을 보여준다.
* Nav

  * 좌측 상단위 로고버튼. 누르면 메인으로 돌아간다.
* FooterAd

  * 특정 페이지 하단항목에 위치. 
  * 추천아이템 3가지를 보여준다.
* Cart

  * 장바구니 페이지
  * 특정 사이즈를 골라야 결제페이지로 연결되며 모든아이템의 사이즈가 선택되지 않았으면 연결되지 않는다.
  * 아이템이 추가될때 마다 CartItem이 생성된다.
    	* 장바구니 단일 아이템을 보여주며 제품에대한 간략한 정보를 보여준다.
* Payment
  * Payment.vue - 장바구니의 데이터를 담아 결제 요청 준비하는 페이지
    * 추후 결제 페이지로 넘어가면 vuex데이터가 사라질 예정이므로, 로컬저장소에 장바구니와 유저 데이터를 저장
  * isApprove.vue - 카카오페이 결제 후, 응답 받은 tid와 pg_token을 이용해 결제 승인을 보내는 페이지
    * 이 시점에 vuex에 데이터가 없어지므로 로컬저장소의 데이터를 가져와 vuex에 재갱신하도록 구성
    * 결제 성공시 OrderComplete로, 실패 혹은 취소시 장바구니 페이지로 재이동
  * OrderComplete.vue - 결제 완료 페이지
    * 주문 번호, 주문명, 주문 시간, 결제 타입 등 주문 관련 정보 출력 및 메인으로 버튼을 누르거나 10초가 지나면 장바구니 데이터와 결제 관련 데이터를 삭제 후 메인 페이지로 이동



## Admin page

* accounts
  * 매장관리를 위한 계정 회원가입, 로그인을 담당한다.
* Admin
  * 상품 관리를 위한 페이지로 새상품 등록이나 등록된 상품리스트, 상품 삭제기능을 수행하는 페이지
  * 상품을 등록하게 되면 ProductForm이 정보를 받아 처리한다.
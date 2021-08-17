# 환경설정

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```



### API Key

```
VUE_APP_YOUTUBE_API_KEY="AIzaSyAZuOI_0j9PNv76ru4xzYmJAIt8v4j1LD0"

.env.local 파일명으로 추가합니다
```



## 컴포넌트 구조



* App
  * Main
  * Ad
    * SearchBar
    * VideoList
  * Adclint
  * Barcode
    * Nav
    * FooterAd
  * PersonalShopper
  * ProductDetail
    * Nav
    * FooterAd
    * ProductLocation
    * ProductSizeChart
    * ProductSizeRecommand

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

  * ?????????????????????????

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

* Cart

  * 장바구니 페이지

* Payment

  * ???????????????



## Admin page

* accounts
  * ????????????????
* Admin
  * ?????????????????
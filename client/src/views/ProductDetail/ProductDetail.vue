<template>
  <div>
    <Nav/>
    <div class="product-box container" :key="productId">
        <img class="product-detail-img" :src=" productDetail.product_image " alt="item1" style="width:45%">
      <div class="text-box">
        <!-- 상품이름 연동필요 -->
        <h2 class="text-box-title">{{ productDetail.product_name }}</h2> 
        <h2>재고정보</h2>
        <div class="size-box">

          <!-- 남자 상의 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'M' && `${productDetail.product_type }` == 1">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <!-- 삼항연산자 stock(재고)유무에 따라 css속성을 바꾼다. 있으면 앞, 없으면 뒤 -->
              <div>
                <span style="text-align: start" >{{manTopSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>
        
          <!-- 남자 하의 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'M' && `${productDetail.product_type }` == 2">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{manBottomSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>                  

          <!-- 여자 상의 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'F' && `${productDetail.product_type }` == 1">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{womanTopSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>        

          <!-- 여자 하의 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'F' && `${productDetail.product_type }` == 2">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{womanBottomSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>

          <!-- 남자 신발 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'M' && `${productDetail.product_type }` == 3">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{manShoesSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>        

          <!-- 여자 신발 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'F' && `${productDetail.product_type }` == 3">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{womanShoesSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>                  

          <!-- 악세서리 -->
          <ul class="size-stock" v-if="`${productDetail.product_type }` == 4">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{accessory[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>          
  
        </div>
        <h2 @click="goToSizeRecommend()" v-if="productDetail.product_type == 1 || productDetail.product_type == 2">사이즈 추천받기</h2>
        <h2 @click="goToSizeChart()">사이즈표</h2>
        <h2 @click="goToLocation()">상품위치 정보</h2>
        <div>
          <b-button v-b-modal.modal-xl variant="primary">상품위치</b-button>
          <b-modal id="modal-xl" size="xl" title="상품위치">
            <div class="modal-img-box">
              <!-- <img src="@/assets/location/totalShop.png" alt="shopMap" class="shop-map background-shop-map"> -->
              <img :src="`${ this.locationPicture}`" alt="specificLocation" class="shop-map blink-shop-map blinking">
            </div>
            <h2 class="modal-h2">해당 상품은 {{this.productLocation}}구역에있습니다.</h2>
          </b-modal>
        </div>
        <div>
          <b-button @click="goToPayment()" variant="primary">구매하기</b-button>
        </div>
      </div>
    </div>
    <h4>PersonalShopper의 추천</h4>
    <FooterAd :productRecommend1="productRecommend1" :productRecommend2="productRecommend2" :productRecommend3="productRecommend3" :productId1="productId1" :productId2="productId2" :productId3="productId3" @selectedProductId="changeProductId"/>
  </div>
</template>

<script>
import FooterAd from '@/views/FooterAd/FooterAd'
import Nav from '@/views/Nav/Nav'
import axios from 'axios'


export default {
  name: 'ProductDetail',
  components: {
    FooterAd,
    Nav,
  },
  data: function() {
    return {
      productDetail: '',  // 상품정보
      productImage: '',  // 상품 이미지
      stocks: '',       // 상품 재고
      productRecommend1: '',    // 리팩토링 필요 (slice => split, props 넘겨주는걸 Array), 추천 1, 2, 3 항목에 해당.
      productRecommend2: '',
      productRecommend3: '',
      manTopSize: ['XS (KR 90)', 'S (KR 95)', 'M (KR 95-100)', 'L (KR 100-105)', 'XL (KR 105-110)'], // 사이즈별 데이터
      womanTopSize: ['XS (KR 44)', 'S (KR 55)', 'M (KR 66)', 'L (KR 77)', 'XL (KR 88)'],
      manBottomSize: ['XS (KR 28)', 'S (KR 30)', 'M (KR 31)', 'L (KR 32)', 'XL (KR 34)'],
      womanBottomSize: ['XS (KR 24)', 'S (KR 26)', 'M (KR 28)', 'L (KR 30)', 'XL (KR 32)'],
      manShoesSize: ['KR 250', 'KR 260', 'KR 270', 'KR 280','KR 290'],
      womanShoesSize: ['KR 230', 'KR 240', 'KR 250', 'KR 260','KR 270'],
      accessory: ['freesize'],
      productId : '301', // 상품 ID
      productId1 : 0,  // 추천 상품 ID
      productId2 : 0,
      productId3 : 0,
      productLocation : '', // 상품위치
      locationPicture : '', // 매장 지도

    }
  },
  methods :{
    goToSizeRecommend(){
      this.$router.push({
        name:'ProductSizeRecommand', 
        params: {
          productRecommend_1: this.productRecommend1,
          productRecommend_2: this.productRecommend2,
          productRecommend_3: this.productRecommend3,
          productId_1: this.productId1,
          productId_2: this.productId2,
          productId_3: this.productId3,
          productDetail: this.productDetail,
        }});
    },
    goToSizeChart(){
      this.$router.push('/ProductSizeChart'); 
    },
    goToLocation(){
      this.$router.push('/ProductDetailLocation'); 
    },
    getProduct: function() { // 상품정보를 받아오는 axios
      const localURL = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL = localURL + this.productId + '/'; //
      
      axios.get(productURL) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.productDetail = res.data; // 상품 상세 정보
          this.productLocation = res.data.location;  // 상품 위치정보 따로 저장
          this.locationPicture = require('@/assets/location/' + res.data.location + '.png'); // 상품 위치정보에 쓸 매장 지도
          this.productRecommend1 = 'http://127.0.0.1:8000/product/' + res.data.style_products.slice(0,3) + '/'; // api 호출에 쓸 연관 추천 상품 주소
          this.productRecommend2 = 'http://127.0.0.1:8000/product/' + res.data.style_products.slice(5,8) + '/';
          this.productRecommend3 = 'http://127.0.0.1:8000/product/' + res.data.style_products.slice(10,14) + '/';
        })
        .then(()=>{ 
          axios.get(this.productRecommend1) // 상품 추천 첫번쨰 아이템 위의 주소를 사용해 id와 이미지 저장.(리팩토링예정)
          .then((res)=>{
            this.productId1 = res.data.product_id;
            this.productRecommend1 = res.data.product_image;
          })
        })
        .then(()=>{                         // 두번째 아이템 호출(리팩토링예정)
          axios.get(this.productRecommend2)
          .then((res)=>{
            this.productId2 = res.data.product_id;
            this.productRecommend2 = res.data.product_image;
          })
          .catch(() => {
            // console.log(err)
          })
        })
        .then(()=>{                   // 세번쨰 아이템 호출(리팩토링예정)
          axios.get(this.productRecommend3)
          .then((res)=>{
            this.productId3 = res.data.product_id;
            this.productRecommend3 = res.data.product_image;
          })
          .catch(() => {
            // console.log(err)
          })
        })
        .catch(() => {
          // console.log(err)
        })
    },
    getStock: function() { // 재고정보를 받아오는 axios
      const localURL = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const stockURL = localURL + this.productId + '/' + 'stocks' +'/';
      axios.get(stockURL)
        .then((res) => {
          this.stocks = res.data.stock;       // stock모델은 size가 필요없다. 바꿔야한다.
        })
        .catch((err) => {
          console.log(err)
        })
    },
    changeProductId: function(selectedProductId) { // 연관 상품 조회시 그 상품 조회 페이지로 이동.
      console.log(selectedProductId)
      this.productId = selectedProductId;
      this.getProduct();
      this.getStock();
    },
    goToPayment: function () {
      this.$router.push({name:'Payment', params: {product: this.productDetail}})
    }
  },
  created: function () { // created로 선언하여 데이터를 갱신한다.
    this.getProduct(); // 상품정보
    this.getStock(); // 재고정보
  },
}

</script>


<style scoped>
.product-box {
  display: flex;
  margin-bottom: 5rem;
}

.product-detail-img {
  margin-right: 5rem;
}

.text-box {
  text-align: center;
}

.size-box {
  display: inline-block;
  width: 100%;
  height: 40%;
}

.size-stock {
  list-style:none;
  padding-left:0px;
  font-size: 2rem;
}

.size-stock li {
  display: flexbox;
}

.size-stock .coming-soon {
  display: flex;
  align-self: end ;
}

.text-box h2 {
  margin: 2rem 0;
}

.text-box .text-box-title {
  margin: 0;
  font-weight: bold;
  font-size: 3rem;
}
.modal-img-box{
  background-image: url("../../assets/location/totalShop.png");
  background-size: 100% 100%;
}
.shop-map {
  width: 100%;
  position: absolute;
}

.modal-h2 {
  text-align: center;
}

.blink-shop-map{
  position: relative;
}


.blinking{ 
  animation:blink 0.25s cubic-bezier(0.68, -0.55, 0.27, 1.55) infinite alternate; 
} 

@keyframes blink{ 
  0% {opacity:0;} 100% {opacity:1;} 
}

</style>
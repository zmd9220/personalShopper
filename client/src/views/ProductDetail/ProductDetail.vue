<template>
  <div>
    <Nav/>
    <div class="product-box" :key="selectedProductID">
      <img class="product-detail-img" :src=" this.$store.state.productDetail.product_image " alt="item1">
      <div class="text-box">
        <!-- 상품이름 연동필요 -->
        <div >
          <p class="text-box-title">{{ this.$store.state.productDetail.product_name }}</p> 
          <h2 style="margin-bottom: 0.5em">재고정보</h2>
        </div>
        <div class="size-box">

          <!-- 남자 상의 -->
          <ul class="size-stock" v-if="`${this.$store.state.productDetail.gender }` == 'M' && `${this.$store.state.productDetail.product_type }` == 1">
            <li :style="[this.$store.state.stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" 
              v-for="stock, i in stocks" :key="i" class="size-text">
              <!-- 삼항연산자 stock(재고)유무에 따라 css속성을 바꾼다. 있으면 앞, 없으면 뒤 -->
              <div class="size-text-box">
                <span >{{manTopSize[i]}}</span>
                <span v-if="stock == 0" > Coming soon</span>
              </div>
            </li>
          </ul>
        
          <!-- 남자 하의 -->
          <ul class="size-stock" v-if="`${this.$store.state.productDetail.gender }` == 'M' && `${this.$store.state.productDetail.product_type }` == 2">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in this.$store.state.stock" :key="i">
              <div class="size-text-box">
                <span>{{manBottomSize[i]}}</span>
                <span v-if="stock == 0"> Coming soon</span>
              </div>
            </li>
          </ul>                  

          <!-- 여자 상의 -->
          <ul class="size-stock" v-if="`${this.$store.state.productDetail.gender }` == 'F' && `${this.$store.state.productDetail.product_type }` == 1">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in this.$store.state.stock" :key="i">
              <div class="size-text-box">
                <span>{{womanTopSize[i]}}</span>
                <span v-if="stock == 0"> Coming soon</span>
              </div>
            </li>
          </ul>        

          <!-- 여자 하의 -->
          <ul class="size-stock" v-if="`${this.$store.state.productDetail.gender }` == 'F' && `${this.$store.state.productDetail.product_type }` == 2">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in this.$store.state.stock" :key="i">
              <div class="size-text-box">
                <span>{{womanBottomSize[i]}}</span>
                <span v-if="stock == 0"> Coming soon</span>
              </div>
            </li>
          </ul>

          <!-- 남자 신발 -->
          <ul class="size-stock" v-if="`${this.$store.state.productDetail.gender }` == 'M' && `${this.$store.state.productDetail.product_type }` == 3">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in this.$store.state.stock" :key="i">
              <div class="size-text-box">
                <span>{{manShoesSize[i]}}</span>
                <span v-if="stock == 0"> Coming soon</span>
              </div>
            </li>
          </ul>        

          <!-- 여자 신발 -->
          <ul class="size-stock" v-if="`${this.$store.state.productDetail.gender }` == 'F' && `${this.$store.state.productDetail.product_type }` == 3">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in this.$store.state.stock" :key="i">
              <div class="size-text-box">
                <span>{{womanShoesSize[i]}}</span>
                <span v-if="stock == 0"> Coming soon</span>
              </div>
            </li>
          </ul>                  

          <!-- 악세서리 -->
          <ul class="size-stock" v-if="`${productDetail.product_type }` == 4">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in this.$store.state.stock" :key="i">
              <div class="size-text-box">
                <span>{{accessory[i]}}</span>
                <span v-if="stock == 0 && i == 0 "> Coming soon</span>
              </div>
            </li>
          </ul>          
  
        </div>
        <div class="button-box">
          <!-- <h2 @click="goToSizeRecommend()" v-if="productDetail.product_type == 1 || productDetail.product_type == 2">사이즈 추천받기</h2> -->
          <b-button variant="primary" class="button-size" @click="buyNow(productDetail)">바로 구매</b-button>
          <b-button variant="primary" class="button-size" @click="addToCart(productDetail)">카트 추가</b-button>
          <b-button @click="goToSizeRecommend()" v-if="this.$store.state.productDetail.product_type == 1 || this.$store.state.productDetail.product_type == 2" 
            variant="primary" class="button-size">사이즈 추천 받기</b-button>
          <!-- <h2 @click="goToSizeChart()">사이즈표</h2> -->
          <!-- <h2 @click="goToLocation()">상품 위치 정보</h2> -->
          <b-button v-b-modal.modal-xl variant="primary" class="button-location" @click="show=true">상품 위치</b-button>
          <b-modal v-model="show" id="modal-xl" header="test"
            centered size="xl" class="location-modal">
            <template #modal-header>
              <div class="mx-auto">
                <p>상품 위치</p>
              </div>
            </template>

            <div class="modal-img-box">
              <!-- <img src="@/assets/location/totalShop.png" alt="shopMap" class="shop-map background-shop-map"> -->
              <img :src="`${ this.locationPicture}`" alt="specificLocation" class="shop-map blink-shop-map blinking">
            </div>
            <p class="modal-h2">해당 상품은 {{this.$store.state.productLocation}}구역에있습니다.</p>

            <template #modal-footer>
              <div class="w-100">
                <b-button
                  variant="primary"
                  size="lg"
                  class="float-right modal-close"
                  @click="show=false"
                >
                  <p>Close</p>
                </b-button>
              </div>
            </template>
          </b-modal>
        </div>
      </div>
    </div>
    
    <div class="footer-row">
      <FooterAd :productRecommend1="productRecommend1" :productRecommend2="productRecommend2" :productRecommend3="productRecommend3" :productId1="productId1" :productId2="productId2" :productId3="productId3" @selectedProductId="changeProductId"/>
    </div>
  </div>
</template>

<script>
import FooterAd from '@/views/FooterAd/FooterAd'
import Nav from '@/views/Nav/Nav'
import axios from 'axios'
import {mapState} from 'vuex'

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
      locationPicture : '', // 매장 지도
      headerBgVariant: 'dark',
      headerTextVariant: 'light',
      show: false,
    }
  },
  computed: {
    ...mapState({
      selectedProductID: state => state.selectedProductID,
      productDetail: state => state.productDetail,
      productLocation: state => state.productLocation,
      productRecommend_1:  state => state.productRecommend_1,
      productRecommend_2:  state => state.productRecommend_2,
      productRecommend_3:  state => state.productRecommend_3,
      productId_1:  state => state.productId_1,
      productId_2:  state => state.productId_2,
      productId_3:  state => state.productId_3,
      stock: state => state.stock,
    })
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
      this.$store.commit('selectProductID', '301');
      // this.$router.push('/ProductSizeChart'); 
    },
    goToLocation(){
      this.$router.push('/ProductDetailLocation'); 
    },
    getProduct: function() { // 상품정보를 받아오는 axios
      const localURL = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL = localURL + this.$store.state.selectedProductID + '/'; //
      
      axios.get(productURL) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.productDetail = res.data; // 상품 상세 정보
          this.$store.commit('productDetail', res.data); // 상품 상세정보
          this.$store.commit('productLocation', res.data.location);
          this.locationPicture = require('@/assets/location/' + this.$store.state.productLocation + '.png'); // 상품 위치정보에 쓸 매장 지도

          // this.productRecommend1 = 'http://127.0.0.1:8000/product/' + res.data.style_products.slice(0,3) + '/'; // api 호출에 쓸 연관 추천 상품 주소
          this.$store.commit('productRecommend_1', 'http://127.0.0.1:8000/product/' + res.data.style_products.slice(0,3) + '/');

          // this.productRecommend2 = 'http://127.0.0.1:8000/product/' + res.data.style_products.slice(5,8) + '/';
          this.$store.commit('productRecommend_2', 'http://127.0.0.1:8000/product/' + res.data.style_products.slice(5,8) + '/');
          
          // this.productRecommend3 = 'http://127.0.0.1:8000/product/' + res.data.style_products.slice(10,14) + '/';
          this.$store.commit('productRecommend_3', 'http://127.0.0.1:8000/product/' + res.data.style_products.slice(10,14) + '/');
        })
        .then(()=>{ 
          axios.get(this.$store.state.productRecommend_1) // 상품 추천 첫번쨰 아이템 위의 주소를 사용해 id와 이미지 저장.(리팩토링예정)
          .then((res)=>{
            // this.productId1 = res.data.product_id;
            this.$store.commit('productId_1', res.data.product_id);
            this.$store.commit('productRecommend_1', res.data.product_image);
          })
        })
        .then(()=>{                         // 두번째 아이템 호출(리팩토링예정)
          axios.get(this.$store.state.productRecommend_2)
          .then((res)=>{
            // this.productId2 = res.data.product_id;
            // this.productRecommend2 = res.data.product_image;
            this.$store.commit('productId_2', res.data.product_id);
            this.$store.commit('productRecommend_2', res.data.product_image);
          })
          .catch(() => {
            // console.log(err)
          })
        })
        .then(()=>{                   // 세번쨰 아이템 호출(리팩토링예정)
          axios.get(this.$store.state.productRecommend_3)
          .then((res)=>{
            // this.productId3 = res.data.product_id;
            // this.productRecommend3 = res.data.product_image;
            this.$store.commit('productId_3', res.data.product_id);
            this.$store.commit('productRecommend_3', res.data.product_image);
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
      const stockURL = localURL + this.$store.state.selectedProductID + '/' + 'stocks' +'/';
      axios.get(stockURL)
        .then((res) => {
          // this.stocks = res.data.stock;       // stock모델은 size가 필요없다. 바꿔야한다.
          this.$store.commit('stock', res.data.stock);
        })
        .catch((err) => {
          console.log(err)
        })
    },
    changeProductId: function(selectedProductId) { // 연관 상품 조회시 그 상품 조회 페이지로 이동.
      this.productId = selectedProductId;
      this.getProduct();
      this.getStock();
    },
    addToCart(productDetail) {
      this.$store.dispatch('cart/addItem', productDetail);
    },
    buyNow(productDetail) {
      this.$store.dispatch('cart/addItem', productDetail);
      this.$router.push({name:'Cart'})
    },
  },
  created: function () { // created로 선언하여 데이터를 갱신한다.
    // this.productId = '201';
    this.getProduct(); // 상품정보
    this.getStock(); // 재고정보
  },
}

</script>


<style scoped>
.product-box {
  display: flex;
  margin-bottom: 5em;
  position: absolute;
  bottom: 35%;
  left: 5%;
  width: 90%;
}

.product-detail-img {
  margin-right: 5em;
  width: 60%;
}

.text-box {
  display: flex;
  flex-direction: column;
  /* align-items: center; */
  justify-content: center;
  text-align: center;
  width: 40%;
}

/* .title-text-area1 {
}

.size-box {
} */

.size-stock {
  display: flex;
  flex-direction: column;
  list-style:none;
  padding-left:0px;
  font-size: 2.5em;
  /* align-self:center; */
  text-align: center;
  margin-bottom: 1em;
}

.size-text {
  justify-content: center;
}

.size-box {
  margin-bottom: 1.5em;
}

.size-text-box {
  display: flex;
  justify-content: space-between;
  /* width: 90%; */
  margin: 0 1.5em 0.5em 1.5em;
}

.text-box h2 {
  margin: 0 0 2em 0;
}

.text-box-title {
  margin: 0 0 1em 0;
}

.button-box {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.button-size {
  margin: 0 0 2em 0;
  font-size: 2em;
  width: 40%;
}

.button-location {
  font-size: 2em;
  width: 30%;
}

.text-box .text-box-title {
  font-weight: bold;
  font-size: 5em;
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
  font-size: 2.5em;
  /* font-weight: bold; */
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

.mx-auto {
  font-size: 3em;
  font-weight: bold;
}

.modal-close {
  font-size: 3em;
}

</style>
<template>
  <div>
    <Nav/>
    <p class="title">"Look" 4 U</p>  
    <!-- 퍼스널 쇼퍼 모델사진들 -->
    <div class="image-area">
      <img :src="productDetail.style_image" alt="look1" class="look-detail">
    </div>
    <div class="look-items-area">
      <p>룩 완성하기</p>
      <div>
        <p>
          <!-- 세트로 구매하는 버튼 -->
          <b-button class="add-items-cart" variant="primary"
            @click="BuyAllItems()">
            <span class="button-text">룩 세트로 구매 <b-icon icon="credit-card" aria-hidden="true"></b-icon></span></b-button>
        </p>
      </div>
      <br>
      <!-- 해당모델이 착용하고 있는 아이템 리스트 -->
      <div class="class=look-items">
        <img class="look-item" @click="goToProductDetail1()" :src="productDetail.product_image" alt="item1">
        <img class="look-item" @click="goToProductDetail2(productId_1)" :src="this.$store.state.productRecommend_1" alt="item2">
        <img class="look-item" @click="goToProductDetail2(productId_2)" :src="this.$store.state.productRecommend_2" alt="item3">
        <img class="look-item" @click="goToProductDetail2(productId_3)" :src="this.$store.state.productRecommend_3" alt="item4">
      </div>
    </div>
  </div>
</template>

<script>
import Nav from '@/views/Nav/Nav'
import {mapState} from 'vuex';
import axios from 'axios'

export default {
  name: 'PersonalShopperDetail',
  components : {
    Nav,
  },
  created: function () { // created로 선언하여 데이터를 갱신한다.
    this.getProduct(); // 상품정보
  },
  data: function() {
    return {
      
    }
  },
  computed: {
    ...mapState(
      ['productDetail', // 메인제품의 상세정보
      'productRecommend_1', // 추천아이템들
      'productRecommend_2',
      'productRecommend_3',
      'selectedProductID', // 메인제품
      'productId_1',
      'productId_2',
      'productId_3',
      ],
      
    ),
  },
  methods: {
    getProduct: function() { // 상품정보를 받아오는 axios      
     axios.get(this.$store.state.productRecommend_1) // 상품 추천 첫번쨰 아이템 위의 주소를 사용해 id와 이미지 저장.
      .then((res)=>{
        this.$store.commit('productId_1', res.data.product_id);
        this.$store.commit('productRecommend_1', res.data.product_image);
      })
      axios.get(this.$store.state.productRecommend_2)
      .then((res)=>{
        this.$store.commit('productId_2', res.data.product_id);
        this.$store.commit('productRecommend_2', res.data.product_image);
      })
     axios.get(this.$store.state.productRecommend_3)
      .then((res)=>{
        this.$store.commit('productId_3', res.data.product_id);
        this.$store.commit('productRecommend_3', res.data.product_image);
      })
      .catch(() => {
            // console.log(err)
          })
    },
    goToProductDetail1: function() { // 디테일 페이지로 이동
      this.$router.push('/ProductDetail')
    },
    goToProductDetail2: function(product_id) { // 디테일 페이지로 이동. 메인제품 변경
      this.$store.commit('selectedProductID', product_id);
      this.$router.push('/ProductDetail')
    },
    addToCart: function(product_id) { // 상품정보를 받아오는 axios
      const localURL = 'http://127.0.0.1:8000/product/'; 
      const productURL = localURL + product_id + '/'; //
      
      axios.get(productURL) 
        .then((res) => {
          this.$store.dispatch('cart/addItem', res.data);
        })
        .catch(() => {
          // console.log(err)
        })
    },
    BuyAllItems(){ // 모델이 착용한 모든 아이템 사기( 장바구니 아이템등록 + 장바구니 화면이동)
      this.$store.dispatch('cart/addItem', this.$store.state.productDetail);
      this.addToCart(this.$store.state.productId_1);
      this.addToCart(this.$store.state.productId_2);
      this.addToCart(this.$store.state.productId_3);
      this.$router.push({name:'Cart'});
    },
    gotoDetail1: function() {                // 메인제품 바꾸고 화면이동
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', this.$store.state.productDetail.product_id);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', this.$store.state.productDetail.product_id);
        this.$emit('selectedProductId', this.$store.state.productDetail.product_id);
      }
    },
    gotoDetail2: function() {                 // 메인제품 바꾸고 화면이동
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', this.$store.state.productId_1);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', this.$store.state.productId_1);
        this.$emit('selectedProductId', this.$store.state.productId_1);
      }
    },
    gotoDetail3: function() {                 // 메인제품 바꾸고 화면이동
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', this.$store.state.productId_2);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', this.$store.state.productId_2);
        this.$emit('selectedProductId', this.$store.state.productId_2);
      }
    },
    gotoDetail4: function() {                 // 메인제품 바꾸고 화면이동
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', this.$store.state.productId_3);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', this.$store.state.productId_3);
        this.$emit('selectedProductId', this.$store.state.productId_3);
      }
    },
  }
}
</script>

<style>
.title {
  font-size: 1.5em;
  font-weight: bold;
  margin-bottom: 0.25em;
}

.img-switch-prev {
  margin: 0 0.5em 0 0;
  font-size: 1.5em;
}

.img-switch-next {
  margin: 0 0 0 0.5em;
  font-size: 1.5em;
}

.look-detail {
  width: 55%;
}

.add-items-cart {
  width: 30%;
  position: fixed;
  right: 5%;
  bottom: 24.5%;
}

.button-text {
  font-size: 0.8em;
}

.look-items-area {
  position: fixed;
  bottom: 0%;
  font-size: 1em;
  font-weight: bold;
}

.look-item {
  display: inline;
  float: left;
  width: 25%;
}
</style>
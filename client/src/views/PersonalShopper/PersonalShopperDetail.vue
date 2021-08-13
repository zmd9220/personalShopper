<template>
  <div>
    <Nav/>
    <p class="title">"Look" 4 U</p>  
    <div class="image-area">
      <b-icon class="img-switch-prev" icon="arrow-left-circle-fill" aria-hidden="true"></b-icon>
      <img :src="productDetail.style_image" alt="look1" class="look-detail">
      <b-icon class="img-switch-next" icon="arrow-right-circle-fill" aria-hidden="true"></b-icon>
    </div>
    <div class="look-items-area">
      <p>룩 완성하기</p>
      <div>
        <p>
          <b-button class="add-items-cart" variant="primary"
            @click="addToCart(productDetail); addToCart(productDetail);
            addToCart(productDetail); addToCart(productDetail);">
            <span class="button-text">룩 세트로 구매 <b-icon icon="credit-card" aria-hidden="true"></b-icon></span></b-button>
        </p>
      </div>
      <br>
      <div class="class=look-items">
        <img class="look-item" :src="productDetail.product_image" alt="item1" @click="gotoDetail1()" >
        <img class="look-item" :src="this.$store.state.productRecommend_1" alt="item2" @click="gotoDetail2()" >
        <img class="look-item" :src="this.$store.state.productRecommend_2" alt="item3" @click="gotoDetail3()" >
        <img class="look-item" :src="this.$store.state.productRecommend_3" alt="item4" @click="gotoDetail4()" >
      </div>
    </div>
    <!-- <FooterAd/> -->
  </div>
</template>

<script>
import Nav from '@/views/Nav/Nav'
import {mapState} from 'vuex';
// import axios from 'axios'

export default {
  name: 'PersonalShopperDetail',
  components : {
    Nav,
  },
  computed: {
    ...mapState(
      ['productDetail'],
      'productRecommend_1',
    ),
  },
  methods: {
    addToCart(productDetail) {
      this.$store.dispatch('cart/addItem', productDetail);
    },
    gotoDetail1: function() {                
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', this.$store.state.productDetail.product_id);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', this.$store.state.productDetail.product_id);
        this.$emit('selectedProductId', this.$store.state.productDetail.product_id);
      }
    },
    gotoDetail2: function() {                 
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', this.$store.state.productId_1);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', this.$store.state.productId_1);
        this.$emit('selectedProductId', this.$store.state.productId_1);
      }
    },
    gotoDetail3: function() {                 
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', this.$store.state.productId_2);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', this.$store.state.productId_2);
        this.$emit('selectedProductId', this.$store.state.productId_2);
      }
    },
    gotoDetail4: function() {                 
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
  font-size: 4em;
  font-weight: bold;
}

.img-switch-prev {
  margin: 0 2em 0 0;
  font-size: 5.5em;
}

.img-switch-next {
  margin: 0 0 0 2em;
  font-size: 5.5em;
}

.look-detail {
  width: 60%;
}

.add-items-cart {
  width: 25%;
  position: fixed;
  right: 10%;
}

.button-text {
  font-size: 3.25em;
}

.look-items-area {
  position: fixed;
  bottom: 0%;
  font-size: 4em;
  font-weight: bold;
}

.look-item {
  display: inline;
  float: left;
  width: 25%;
  /* margin: 0 0 0 0.2em; */
}
</style>
<template>
  <div>
    <Nav/>
    <p class="page-title">PersonalShopper</p>
    <!-- 퍼스널 쇼퍼 아이템들 -->
    <img class="product-detail-img" :src=" this.productDetail1.style_image" alt="personal1" @click="goToPersonalShopperDetail1()"> 
    <img class="product-detail-img" :src=" this.productDetail2.style_image" alt="personal1" @click="goToPersonalShopperDetail2()">
    <img class="product-detail-img" :src=" this.productDetail3.style_image" alt="personal1" @click="goToPersonalShopperDetail3()">
    <img class="product-detail-img" :src=" this.productDetail4.style_image" alt="personal1" @click="goToPersonalShopperDetail4()">
  </div>

</template>

<script>
import Nav from '@/views/Nav/Nav'
import axios from 'axios'
import { mapState  } from 'vuex'

export default {
  data: function () {
    return {
      productDetail1: '',  // 상품정보
      productDetail2: '',  // 상품정보
      productDetail3: '',  // 상품정보
      productDetail4: '',  // 상품정보
    }
  },
  components : {
    Nav,
  },
  computed: {
    ...mapState ({

      selectedProductID: state => state.selectedProductID, // 메인 제품
      productId_1: state => state.productId_1,
      productId_2: state => state.productId_2,
      productId_3: state => state.productId_3,
      }
    ),
    },
  methods: {
    getProduct: function() { // 상품정보를 받아오는 axios
      const localURL1 = 'http://127.0.0.1:8000/product/'; 
      const productURL1 = localURL1 + this.selectedProductID + '/'; //
      
      axios.get(productURL1) 
        .then((res) => {
          this.productDetail1 = res.data; // 상품 상세 정보
        })
        .catch(() => {
          // console.log(err)
        });

      const localURL2 = 'http://127.0.0.1:8000/product/'; 
      const productURL2 = localURL2 + this.productId_1 + '/'; //
      
      axios.get(productURL2) 
        .then((res) => {
          this.productDetail2 = res.data; // 상품 상세 정보
        })
        .catch(() => {
          // console.log(err)
        });

      const localURL3 = 'http://127.0.0.1:8000/product/'; 
      const productURL3 = localURL3 + this.productId_2 + '/'; 
      
      axios.get(productURL3) 
        .then((res) => {
          this.productDetail3 = res.data; // 상품 상세 정보
        })
        .catch(() => {
          // console.log(err)
        });

      const localURL4 = 'http://127.0.0.1:8000/product/'; 
      const productURL4 = localURL4 + this.productId_3 + '/'; 
      
      axios.get(productURL4) 
        .then((res) => {
          this.productDetail4 = res.data; // 상품 상세 정보
        })
        .catch(() => {
          // console.log(err)
        });
    },
    goToPersonalShopperDetail1(){ // 선택항목을 고를시 Detail 페이지로 이동. 추천아이템들을 변경해준다.
      this.$router.push('/PersonalShopperDetail'); 
      this.$store.commit('productRecommend_1', 'http://127.0.0.1:8000/product/' + this.productDetail1.style_products.slice(0,3) + '/');
      this.$store.commit('productRecommend_2', 'http://127.0.0.1:8000/product/' + this.productDetail1.style_products.slice(5,8) + '/');
      this.$store.commit('productRecommend_3', 'http://127.0.0.1:8000/product/' + this.productDetail1.style_products.slice(10,14) + '/');
      this.$store.commit('productDetail', this.productDetail1); // 상품 상세정보
    },
    goToPersonalShopperDetail2(){ // 선택항목을 고를시 Detail 페이지로 이동. 추천아이템들을 변경해준다.
      this.$router.push('/PersonalShopperDetail'); 
      this.$store.commit('productRecommend_1', 'http://127.0.0.1:8000/product/' + this.productDetail2.style_products.slice(0,3) + '/');     
      this.$store.commit('productRecommend_2', 'http://127.0.0.1:8000/product/' + this.productDetail2.style_products.slice(5,8) + '/');    
      this.$store.commit('productRecommend_3', 'http://127.0.0.1:8000/product/' + this.productDetail2.style_products.slice(10,14) + '/');
      this.$store.commit('productDetail', this.productDetail2); // 상품 상세정보
      this.$store.commit('selectedProductID', this.productDetail2.product_id);
    },
    goToPersonalShopperDetail3(){ // 선택항목을 고를시 Detail 페이지로 이동. 추천아이템들을 변경해준다.
      this.$router.push('/PersonalShopperDetail'); 
      this.$store.commit('productRecommend_1', 'http://127.0.0.1:8000/product/' + this.productDetail3.style_products.slice(0,3) + '/');         
      this.$store.commit('productRecommend_2', 'http://127.0.0.1:8000/product/' + this.productDetail3.style_products.slice(5,8) + '/');    
      this.$store.commit('productRecommend_3', 'http://127.0.0.1:8000/product/' + this.productDetail3.style_products.slice(10,14) + '/');
      this.$store.commit('productDetail', this.productDetail3); // 상품 상세정보
      this.$store.commit('selectedProductID', this.productDetail3.product_id);
    },
    goToPersonalShopperDetail4(){ // 선택항목을 고를시 Detail 페이지로 이동. 추천아이템들을 변경해준다.
      this.$router.push('/PersonalShopperDetail'); 
      this.$store.commit('productRecommend_1', 'http://127.0.0.1:8000/product/' + this.productDetail4.style_products.slice(0,3) + '/');         
      this.$store.commit('productRecommend_2', 'http://127.0.0.1:8000/product/' + this.productDetail4.style_products.slice(5,8) + '/');    
      this.$store.commit('productRecommend_3', 'http://127.0.0.1:8000/product/' + this.productDetail4.style_products.slice(10,14) + '/');
      this.$store.commit('productDetail', this.productDetail4); // 상품 상세정보
      this.$store.commit('selectedProductID', this.productDetail4.product_id);
    },
  },
  created: function () {
    this.getProduct(); // 상품정보
  },
};
</script>

<style>

.page-title {
  text-align: end;
  margin-right: 1em;
  font-weight: bold;
  font-size: 1.5em;
}

.product-detail-img {
  width: 44%;
  margin: 0.25em;
}

.footer-text {
  font-size: 1em;
  margin-top: 1em;
}

</style>
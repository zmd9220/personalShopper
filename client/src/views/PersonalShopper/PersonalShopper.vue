<template>
  <div>
    <h4 class="title">PersonalShopper</h4>
    <img class="product-detail-img" :src=" this.productDetail1.style_image" alt="personal1" style="width:47%" @click="goToPersonalShopperDetail1()"> 
    <img class="product-detail-img" :src=" this.productDetail2.style_image" alt="personal1" style="width:47%" @click="goToPersonalShopperDetail2()">
    <img class="product-detail-img" :src=" this.productDetail3.style_image" alt="personal1" style="width:47%" @click="goToPersonalShopperDetail3()">
    <img class="product-detail-img" :src=" this.productDetail4.style_image" alt="personal1" style="width:47%" @click="goToPersonalShopperDetail4()">
  </div>

</template>

<script>
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
  computed: {
    ...mapState ({

      selectedProductID: state => state.selectedProductID,
      productId_1: state => state.productId_1,
      productId_2: state => state.productId_2,
      productId_3: state => state.productId_3,
      }
    ),
    },
  methods: {
    getProduct: function() { // 상품정보를 받아오는 axios
      const localURL1 = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL1 = localURL1 + this.selectedProductID + '/'; //
      
      axios.get(productURL1) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.productDetail1 = res.data; // 상품 상세 정보
        })
        .catch(() => {
          // console.log(err)
        });

      const localURL2 = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL2 = localURL2 + this.productId_1 + '/'; //
      
      axios.get(productURL2) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.productDetail2 = res.data; // 상품 상세 정보
        })
        .catch(() => {
          // console.log(err)
        });

      const localURL3 = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL3 = localURL3 + this.productId_2 + '/'; //
      
      axios.get(productURL3) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.productDetail3 = res.data; // 상품 상세 정보
        })
        .catch(() => {
          // console.log(err)
        });

      const localURL4 = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL4 = localURL4 + this.productId_3 + '/'; //
      
      axios.get(productURL4) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.productDetail4 = res.data; // 상품 상세 정보
        })
        .catch(() => {
          // console.log(err)
        });
    },
    goToPersonalShopperDetail1(){
      this.$router.push('/PersonalShopperDetail'); 
      this.$store.commit('productRecommend_1', 'http://127.0.0.1:8000/product/' + this.productDetail1.style_products.slice(0,3) + '/');
      this.$store.commit('productRecommend_2', 'http://127.0.0.1:8000/product/' + this.productDetail1.style_products.slice(5,8) + '/');
      this.$store.commit('productRecommend_3', 'http://127.0.0.1:8000/product/' + this.productDetail1.style_products.slice(10,14) + '/');
      this.$store.commit('productDetail', this.productDetail1); // 상품 상세정보
    },
    goToPersonalShopperDetail2(){
      this.$router.push('/PersonalShopperDetail'); 
      this.$store.commit('productRecommend_1', 'http://127.0.0.1:8000/product/' + this.productDetail2.style_products.slice(0,3) + '/');     
      this.$store.commit('productRecommend_2', 'http://127.0.0.1:8000/product/' + this.productDetail2.style_products.slice(5,8) + '/');    
      this.$store.commit('productRecommend_3', 'http://127.0.0.1:8000/product/' + this.productDetail2.style_products.slice(10,14) + '/');
      this.$store.commit('productDetail', this.productDetail2); // 상품 상세정보
      this.$store.commit('selectedProductID', this.productDetail2.product_id);
    },
    goToPersonalShopperDetail3(){
      this.$router.push('/PersonalShopperDetail'); 
      this.$store.commit('productRecommend_1', 'http://127.0.0.1:8000/product/' + this.productDetail3.style_products.slice(0,3) + '/');         
      this.$store.commit('productRecommend_2', 'http://127.0.0.1:8000/product/' + this.productDetail3.style_products.slice(5,8) + '/');    
      this.$store.commit('productRecommend_3', 'http://127.0.0.1:8000/product/' + this.productDetail3.style_products.slice(10,14) + '/');
      this.$store.commit('productDetail', this.productDetail3); // 상품 상세정보
      this.$store.commit('selectedProductID', this.productDetail3.product_id);
    },
    goToPersonalShopperDetail4(){
      this.$router.push('/PersonalShopperDetail'); 
      this.$store.commit('productRecommend_1', 'http://127.0.0.1:8000/product/' + this.productDetail4.style_products.slice(0,3) + '/');         
      this.$store.commit('productRecommend_2', 'http://127.0.0.1:8000/product/' + this.productDetail4.style_products.slice(5,8) + '/');    
      this.$store.commit('productRecommend_3', 'http://127.0.0.1:8000/product/' + this.productDetail4.style_products.slice(10,14) + '/');
      this.$store.commit('productDetail', this.productDetail4); // 상품 상세정보
      this.$store.commit('selectedProductID', this.productDetail4.product_id);
    },
  },
  created: function () {
    // created로 선언하여 데이터를 갱신한다.
    // this.productId = '201';
    this.getProduct(); // 상품정보
  },
};
</script>

<style>
.title {
  font-size: 5rem;
}

.product-detail-img {
  margin: 1rem;
}

</style>
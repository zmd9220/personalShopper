<template>
  <div>
    <h4>PersonalShopper</h4>
    <!-- <div>{{this.$store.state.user}}</div> -->

    <img class="product-detail-img" :src=" this.productDetail1.style_image" alt="personal1" style="width:50%"> 
    <img class="product-detail-img" :src=" this.productDetail2.style_image" alt="personal1" style="width:50%">
    <img class="product-detail-img" :src=" this.productDetail3.style_image" alt="personal1" style="width:50%">
    <img class="product-detail-img" :src=" this.productDetail4.style_image" alt="personal1" style="width:50%">

    <!-- <video autoplay >
      <source src="@/assets/ad/y2mate.com - ZARA WOMAN  Spring Summer 2021 Campaign_1080p.mp4">
    </video> -->

    <div>
      
      
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const recommendProductData = JSON.parse(localStorage.getItem('recommendData'))



export default {
  data: function() {
    return {
      productDetail1: '',  // 상품정보
      productDetail2: '',  // 상품정보
      productDetail3: '',  // 상품정보
      productDetail4: '',  // 상품정보
      recommendProductId: recommendProductData,
    }
  },
  computed: {
    videoElement () {
      return this.$refs.video;
    }, 
  },
  methods: {
    getProduct: function() { // 상품정보를 받아오는 axios
      const localURL1 = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL1 = localURL1 + this.recommendProductId['A'] + '/'; //
      
      axios.get(productURL1) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.productDetail1 = res.data; // 상품 상세 정보
          this.$store.commit('1', res.data); // 상품 상세정보
        })
        .catch(() => {
          // console.log(err)
        })

      const localURL2 = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL2 = localURL2 + this.recommendProductId['B'] + '/'; //
      
      axios.get(productURL2) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.productDetail2 = res.data; // 상품 상세 정보
          this.$store.commit('productDetail', res.data); // 상품 상세정보
        })
        .catch(() => {
          // console.log(err)
        })

      const localURL3 = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL3 = localURL3 + this.recommendProductId['C'] + '/'; //
      
      axios.get(productURL3) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.productDetail3 = res.data; // 상품 상세 정보
          this.$store.commit('productDetail', res.data); // 상품 상세정보
        })
        .catch(() => {
          // console.log(err)
        })

      const localURL4 = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL4 = localURL4 + this.recommendProductId['D'] + '/'; //
      
      axios.get(productURL4) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.productDetail4 = res.data; // 상품 상세 정보
          this.$store.commit('productDetail', res.data); // 상품 상세정보
        })
        .catch(() => {
          // console.log(err)
        })
    },
  },
  created: function () { // created로 선언하여 데이터를 갱신한다.
    // this.productId = '201';
    this.getProduct(); // 상품정보
  },
}
</script>

<style>

</style>
<template>
  <div>
    <Nav/>

    <div class="pay-card">
      <b-card no-body class="overflow-hidden" style="max-width: 540px;">
        <b-row no-gutters>
          <b-col md="6">
            <b-card-img src="https://picsum.photos/400/400/?image=20" alt="Image" class="rounded-0"></b-card-img>
          </b-col>
          <b-col md="6">
            <b-card-body title="Horizontal Card">
              <b-card-text>
                This is a wider card with supporting text as a natural lead-in to additional content.
                This content is a little bit longer.
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>

      <b-card img-src="https://placekitten.com/300/300" img-alt="Card image" img-left class="mb-3">
        <b-card-text>
          Some quick example text to build on the card and make up the bulk of the card's content.
        </b-card-text>
      </b-card>
    </div>

  </div>
</template>


<script>
import Nav from '@/views/Nav/Nav'
import axios from 'axios'
// import {mapState} from 'vuex'

export default {
  name: 'PaymentPage',
  components: {
    Nav,
  },
  data: function() {
    return {
      productId : '301',
    }
  },
  methods :{
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
    }
  }
}
</script>


<style>
.pay-card {
  /* display: ; */
  width: 80%;
  
}
</style>
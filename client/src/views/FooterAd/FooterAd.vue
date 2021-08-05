<template>
  <div>
    <div class="footer-row">
      <!-- 추천항목이 있을시 보여주고 없으면 디폴트데이터 보여주기. 리팩토링가능해보임. v-if 빼고 기본을 디폴트 데이터가 넘어오면 덮어씌우는형식으로 -->
      <div class="column" v-if="productRecommend1.slice(0,5) == 'https'">
        <img :src="productRecommend1" alt="item3" style="width: 100%" @click="gotoDetail1()" >
      </div>

      <div class="column" v-if="productRecommend1.slice(0,5) != 'https'">
        <img src="@/assets/dummydata/101.png" alt="item1" style="width: 100%" @click="gotoDetailDefault1()" >
      </div>

      <div class="column" v-if="productRecommend2.slice(0,5) == 'https'">
        <img :src="this.productRecommend2" alt="item3" style="width: 100%" @click="gotoDetail2()" >
      </div>

      <div class="column" v-if="productRecommend2.slice(0,5) != 'https'">
        <img src="@/assets/dummydata/102.png" alt="item2" style="width: 100%" @click="gotoDetailDefault2()" >
      </div>

      <div class="column" v-if="productRecommend3.slice(0,5) == 'https'">
        <img :src="this.productRecommend3" alt="item3" style="width: 100%" @click="gotoDetail3()" >
      </div>

      <div class="column" v-if="productRecommend3.slice(0,5) != 'https'">
        <img src="@/assets/dummydata/103.png" alt="item3" style="width: 100%" @click="gotoDetailDefault3()" >
      </div>
    </div>
  </div>

</template>

<script>
// import axios from 'axios'

export default {
  props: {
    productRecommend1 : { // 추천 1,2,3
      type: String,
    },
    productRecommend2 : {
      type: String,
    },
    productRecommend3 : {
      type: String,
    },
    productId1 : {
      type: Number,
    }, 
    productId2 : {
      type: Number,
    }, 
    productId3 : {
      type: Number,
    }, 
  },
  data: function() {
    return {
      Recommend1: '',
      Recommend2: '',
      Recommend3: '',
    }
  },
  methods:{
    gotoDetail1: function() {                 //리팩토링 필요
      const productId1 = this.productId1;
      this.$emit('selectedProductId', productId1);
    },
    gotoDetail2: function() {                 //리팩토링 필요
      const productId2 = this.productId2;
      this.$emit('selectedProductId', productId2);
    },
    gotoDetail3: function() {                 //리팩토링 필요
      const productId3 = this.productId3;
      this.$emit('selectedProductId', productId3);
    },
    gotoDetailDefault1: function() {                 //리팩토링 필요
      this.$emit('selectedProductId', '101');
    },
    gotoDetailDefault2: function() {                 //리팩토링 필요
      this.$emit('selectedProductId', '102');
    },
    gotoDetailDefault3: function() {                 //리팩토링 필요
      this.$emit('selectedProductId', '103');
    },
    // getProduct1: function() { // 상품정보를 받아오는 axios
      // const localURL = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      // const productURL = localURL + this.Recommend1 + '/'; //
      // console.log(this.productRecommend1)
      // console.log(this.productRecommend2)
      // console.log(this.productRecommend3)
      // axios.get(this.productRecommend1) // 리팩토링 필요.
      //   .then((res) => {
      //     console.log(res.data.product_image);
      //     this.Recommend1 = res.data.product_image;
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   });
      // axios.get(this.productRecommend2) // 리팩토링 필요.
      //   .then((res) => {
      //     // console.log(res.data.product_image)
      //     // this.productDetail = res.data;
      //     this.Recommend2 = res.data.product_image;
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   });
      // axios.get(this.productRecommend3) // 리팩토링 필요.
      //   .then((res) => {
      //     // console.log(res.data.product_image)
      //     // this.productDetail = res.data;
      //     this.Recommend3 = res.data.product_image;
      //   })
      //   .catch((err) => {
      //     console.log(err)
      //   })
    // },
  },
  // mounted: function () { // created로 선언하여 데이터를 갱신한다.
  //   // console.log(this.productRecommend1)
  //   // this.getProduct1();
  //   // this.getProduct(this.productRecommend2);
  //   // this.getProduct(this.productRecommend3);
  // },
}
</script>

<style scoped>

.footer-row {
  display: flex;
  content: "";
  clear: both;
  width: 100%;
}

.column {
  display: inline;
  float: left;
  margin: 0 0.3rem;
  width: 33.3%;
}


</style>
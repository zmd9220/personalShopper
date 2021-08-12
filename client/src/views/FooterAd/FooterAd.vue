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
import {mapState} from 'vuex'

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
    productId1 : { // 추천 ID 1,2,3
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
  computed: {
    ...mapState({
      selectedProductID: state => state.selectedProductID
    })
  },
  methods:{
    gotoDetail1: function() {                 //리팩토링 예정 (디폴트 데이터가 넘어오면 덮어씌우는형식으로)
      const productId1 = this.productId1.toString();
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', productId1);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', productId1);
        this.$emit('selectedProductId', productId1);
      }
    },
    gotoDetail2: function() {                 //리팩토링 예정
      const productId2 = this.productId2.toString();
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', productId2);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', productId2);
        this.$emit('selectedProductId', productId2);
      }
    },
    gotoDetail3: function() {                 //리팩토링 예정
      const productId3 = this.productId3.toString();
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', productId3);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', productId3);
        this.$emit('selectedProductId', productId3);
      }
    },
    gotoDetailDefault1: function() {                 //리팩토링 예정
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', '101');
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', '101');
        this.$emit('selectedProductId', '101');
      }
    },
    gotoDetailDefault2: function() {                 //리팩토링 예정
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', '102');
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', '102');
        this.$emit('selectedProductId', '102');
      }
    },
    gotoDetailDefault3: function() {                 //리팩토링 예정
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectProductID', '103');
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectProductID', '103');
        this.$emit('selectedProductId', '103');
      }
    },
  },
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
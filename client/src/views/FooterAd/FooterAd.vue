<template>
  <div>
    <div class="footer">
      <div class="footer-text">
        <p>PersonalShopper의 추천</p>
      </div>
      <div class="footer-row">
        
        <div class="column">
          <img :src="this.$store.state.productRecommend_1" alt="item3" style="width: 100%" @click="gotoDetail1()" >
        </div>

        <div class="column">
          <img :src="this.$store.state.productRecommend_2" alt="item3" style="width: 100%" @click="gotoDetail2()" >
        </div>

        <div class="column">
          <img :src="this.$store.state.productRecommend_3" alt="item3" style="width: 100%" @click="gotoDetail3()" >
        </div>

      </div>
    </div>
  </div>

</template>

<script>
import {mapState} from 'vuex'

export default {
  props: {
  },
  data: function() {
    return {
    }
  },

  computed: {
    ...mapState({
      selectedProductID: state => state.selectedProductID,
      productRecommend_1: state => state.productRecommend_1,
      productRecommend_2: state => state.productRecommend_2,
      productRecommend_3: state => state.productRecommend_3,
      productId_1: state => state.productId_1,
      productId_2: state => state.productId_2,
      productId_3: state => state.productId_3,
    })
  },
  methods:{
    gotoDetail1: function() {                
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectedProductID', this.$store.state.productId_1);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectedProductID', this.$store.state.productId_1);
        this.$emit('selectedProductId', this.$store.state.productId_1);
      }
    },
    gotoDetail2: function() {                 
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectedProductID', this.$store.state.productId_2);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectedProductID', this.$store.state.productId_2);
        this.$emit('selectedProductId', this.$store.state.productId_2);
      }
    },
    gotoDetail3: function() {                 
      if (this.$route.path !== '/ProductDetail' ) {
        this.$store.commit('selectedProductID', this.$store.state.productId_3);
        this.$router.push({name:'ProductDetail'});
      } else {
        this.$store.commit('selectedProductID', this.$store.state.productId_3);
        this.$emit('selectedProductId', this.$store.state.productId_3);
      }
    },
  },
}
</script>

<style scoped>

.footer {
  display:contents;

}

.footer-text {
  font-size: 5rem;
  position: fixed;
  bottom: 30%;
  left: 0%;
  right: 0%;
}

.footer-row {
  display: flex;
  /* content: ""; */
  /* clear: both; */
  width: 100%;
  position: fixed;
  bottom: 0%;
  font-size: 5em;
  /* left: 0%;
  right: 0%; */
}

.column {
  display: inline;
  float: left;
  margin: 0 0.3rem;
  width: 33.3%;
}


</style>
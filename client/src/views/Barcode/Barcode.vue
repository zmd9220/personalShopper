<template>
  <div>
    <Nav/>
    <div class="blank-box"></div>
    <h4>상품의 바코드를</h4>
    <h4>인식기에 보여주세요</h4>
    <div class="blank-box"></div>
    <h4>PersonalShopper의 추천</h4>
    <FooterAd :productRecommend1="productRecommend1" :productRecommend2="productRecommend2" :productRecommend3="productRecommend3" :productId1="productId1" :productId2="productId2" :productId3="productId3" @selectedProductId="changeProductId"/>
  </div>
</template>

<script>
import FooterAd from '@/views/FooterAd/FooterAd'
import Nav from '@/views/Nav/Nav'


export default {
  name: 'Barcode',
  components: {
    FooterAd,
    Nav,
  },
  data: function() {
    return {
      productRecommend1: '',
      productRecommend2: '',
      productRecommend3: '',
    }
  },
  methods: {
    changeProductId(payload){
      console.log(payload)
      this.$router.push({
        name:'ProductDetail', 
        params: {
          passProductID: payload,
      }});
    }
  }
}
</script>

<style scoped>
.blank-box {
  height: 15rem;
}
</style>
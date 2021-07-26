<template>
  <div>
    <Nav/>
    <div class="product-box container">
      <img class="product-detail-img" src="@/assets/item1.png" alt="item1" style="width:45%">
      <div class="text-box">
        <!-- 상품이름 연동필요 -->
        <h2 class="text-box-title">스트럭처 셔츠</h2> 
        <h2>재고정보</h2>
        <div class="size-box"></div>
        <h2 @click="goToSizeRecommend()">사이즈 추천받기</h2>
        <h2 @click="goToSizeChart()">사이즈표</h2>
        <h2 @click="goToLocation()">상품위치 정보</h2>
      </div>
    </div>

    
    <h4>PersonalShopper의 추천</h4>
    <FooterAd/>
  </div>
</template>

<script>
import FooterAd from '@/views/FooterAd/FooterAd'
import Nav from '@/views/Nav/Nav'

export default {
  name: 'ProductDetail',
  components: {
    FooterAd,
    Nav,
  },
  methods :{
    goToSizeRecommend(){
      this.$router.push('/ProductSizeRecommand'); 
    },
    goToSizeChart(){
      this.$router.push('/ProductSizeChart'); 
    },
    goToLocation(){
      this.$router.push('/ProductDetailLocation'); 
    },
  },
}
</script>

<style scoped>
.product-box {
  display: flex;
  margin-bottom: 5rem;
}

.product-detail-img {
  margin-right: 5rem;
}

.text-box {
  text-align: center;
}

.size-box {
  display: inline-block;
  width: 100%;
  height: 40%;
  background: rgba(66, 60, 60, 0.781);
}

.text-box h2 {
  margin: 2rem 0;
}

.text-box .text-box-title {
  margin: 0;
  font-weight: bold;
  font-size: 3rem;
}
</style>
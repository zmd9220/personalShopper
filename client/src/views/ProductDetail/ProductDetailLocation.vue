<template>
  <div>
    <Nav/>
    <div class="product-box container">
      <img class="product-detail-img" src="@/assets/item1.png" alt="item1" style="width:45%">
    </div>

    <div class="text-box">
      <h2 class="location-text">셔츠는 A구역에 있습니다.</h2>
    </div>

    <div class="blank-box"></div>
    <h4>PersonalShopper의 추천</h4>
    <FooterAd/>
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
}
</script>

<style scoped>
.product-detail-img {
  display: block;
  margin: auto;
}

.text-box {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 5rem 0;
}

.text-box .location-text {
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: 3rem;
}

.blank-box {
  height: 15rem;
}
</style>
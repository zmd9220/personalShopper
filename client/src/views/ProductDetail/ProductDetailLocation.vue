<template>
  <div>
    <Nav/>
    <div class="ProductBox container">
      <img class="ProductDetailImg" src="@/assets/item1.png" alt="item1" style="width:45%">
    </div>

    <div>
      <h1>셔츠는 A구역에 있습니다.</h1>
    </div>

    <div class="BlankBox"></div>
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

<style>
.BlankBox {
  height: 15rem;
}
</style>
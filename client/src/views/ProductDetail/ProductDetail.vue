<template>
  <div>
    <Nav/>
    <div class="ProductBox container">
      <img class="ProductDetailImg" src="@/assets/item1.png" alt="item1" style="width:45%">
      <div class="TextBox">
        <div class=""> 상품이름</div>
        <div class=""> 상품이름</div>
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
  name: 'Barcode',
  components: {
    FooterAd,
    Nav,
  },
}
</script>

<style>
.ProductBox {
  display: flex;
  margin-bottom: 5rem;
}

.ProductDetailImg {
  margin-right: 5rem;
}

.TextBox {
  text-align: center;
}

</style>
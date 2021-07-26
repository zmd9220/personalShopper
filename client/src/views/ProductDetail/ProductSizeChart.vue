<template>
  <div>
    <Nav/>
    <div class="product-box container">
      <div class="text-box">
        <!-- 상품이름 연동필요 -->
        <h1 class="text-box-title">스트럭처 셔츠</h1>
      </div>
      <img class="ProductDetailImg" src="@/assets/item1.png" alt="item1" style="width:45%">
    </div>
    <img class="" src="@/assets/sizechart.png" alt="item1" style="width:100%">
    <img class="" src="@/assets/sizeguide.png" alt="item1" style="width:100%">

    
    
  </div>
</template>

<script>

import Nav from '@/views/Nav/Nav'

export default {
  name: 'ProductSizeChart',
  components: {

    Nav,
  },
}
</script>

<style scoped>
.product-box {
  display: flex;
  margin-bottom: 5rem;
}

.text-box {
  display: flex;
  text-align: center;
  margin-right: 5rem;
  width: 50vh;
}

.text-box .text-box-title {
  display: flex;
  margin: 0;
  font-weight: bold;
  font-size: 3rem;
  justify-content: center;
  align-items: center;
}

</style>
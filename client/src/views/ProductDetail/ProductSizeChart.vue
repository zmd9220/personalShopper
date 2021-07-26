<template>
  <div>
    <Nav/>
    <div class="ProductBox container">
      <div class="TextBox">
        <h1>상품이름</h1>
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
  name: 'Barcode',
  components: {

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
  
}

.TextBox {
  text-align: center;
  margin-right: 5rem;
}

</style>
<template>
  <div>

    <div class="footer-row" v-if="!style_products">



    </div>

    
    <div class="footer-row">
      <div class="column" v-if="productRecommend1">
        <img :src="`${productRecommend1}`" alt="item3" style="width: 100%">
      </div>

      <div class="column" v-if="!productRecommend1">
        <img src="@/assets/item1.png" alt="item1" style="width: 100%">
      </div>

      <div class="column" v-if="productRecommend2">
        <img :src="`${productRecommend2}`" alt="item3" style="width: 100%">
      </div>

      <div class="column" v-if="!productRecommend2">
        <img src="@/assets/item2.png" alt="item2" style="width: 100%">
      </div>

      <div class="column" v-if="productRecommend3">
        <img :src="`${productRecommend3}`" alt="item3" style="width: 100%">
      </div>

      <div class="column" v-if="!productRecommend3">
        <img src="@/assets/item3.png" alt="item3" style="width: 100%">
      </div>
    </div>
  </div>

</template>

<script>
export default {
  props: {
    style_products: {
      type: String,
    },
    productRecommend1 : {
      type: String,
    },
    productRecommend2 : {
      type: String,
    },
    productRecommend3 : {
      type: String,
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
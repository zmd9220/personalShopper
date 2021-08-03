<template>
  <div>
    <div class="footer-row">
      <!-- 추천항목이 있을시 보여주고 없으면 디폴트데이터 보여주기. 리팩토링가능해보임. v-if 빼고 기본을 디폴트 데이터가 넘어오면 덮어씌우는형식으로 -->
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
    productRecommend1 : { // 추천 1,2,3
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
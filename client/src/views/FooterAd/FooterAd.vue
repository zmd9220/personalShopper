<template>

  <div class="row">
    <div class="column">
      <img src="@/assets/item1.png" alt="item1">
    </div>
    <div class="column">
      <img src="@/assets/item2.png" alt="item2">
    </div>
    <div class="column">
      <img src="@/assets/item3.png" alt="item3">
    </div>
</div>

</template>

<script>
export default {
  props: {
    style_products: [String],
    },
}
</script>

<style scoped>

.row {
  display: flex;
  /* content: ""; */
  clear: both;
  width: 100%;
}

.column {
  display: inline;
  /* float: left; */
  width: 33.33%;
  padding: 5px;
}


</style>
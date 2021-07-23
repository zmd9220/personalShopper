<template>

  <div class="row">
    <div class="column">
      <img src="@/assets/item1.png" alt="item1" style="width:100%">
    </div>
    <div class="column">
      <img src="@/assets/item2.png" alt="item2" style="width:100%">
    </div>
    <div class="column">
      <img src="@/assets/item3.png" alt="item3" style="width:100%">
    </div>
</div>

</template>

<script>
export default {

}
</script>

<style>


/* Three image containers (use 25% for four, and 50% for two, etc) / */
.column {
  float: left;
  width: 33.33%;
  padding: 5px;
}

/* / Clear floats after image containers */
.row {
  display: flex;
  content: "";
  clear: both;
}

</style>
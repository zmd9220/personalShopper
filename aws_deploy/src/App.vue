<template>
  <div id="app">
    <video controls class="iframe" controlsList="nodownload">
      <source src="@/assets/공통프로젝트 UCC(최종).mp4">
    </video>
    <img class="ppt-image" alt="Personal-Shopper-PPT" src="./assets/Personal-Shopper-PPT_2.jpg">
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
html {
  background-color: rgb(14, 13, 13);
}
#app {
  text-align: center;
  margin-top: 3vh;
}

.ppt-image {
  width: 60%;
}

.iframe {
width: 60%;
}

</style>

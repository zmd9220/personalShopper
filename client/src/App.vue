<template>
  <div id="app">
    <!-- 개발용 라우터 뷰 -->
    <div id="nav">
      <router-link to="/">Main</router-link> |
      <router-link to="/Ad">Ad</router-link> |
      <router-link to="/AdClient">AdClient</router-link> |
      <router-link to="/Barcode">Barcode</router-link> |
      <router-link to="/ProductDetail">ProductDetail</router-link> |
      <router-link to="/ProductSizeChart">ProductSizeChart</router-link> | 
      <router-link to="/ProductDetailLocation">ProductDetailLocation</router-link> | 
      <router-link to="/ProductSizeRecommand">ProductSizeRecommand</router-link> | 
      <router-link to="/PersonalShopper">PersonalShopper</router-link> | 
    </div>
    <router-view/>
  </div>
</template>

<style lang="scss">
@import "~@/assets/scss/vendors/bootstrap-vue/index";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

<template>
  <div id="app">
    <!-- 개발용 라우터 뷰 -->
    <div id="nav">
      <router-link to="/">Main</router-link> |
      <!-- <router-link to="/Ad">Ad</router-link> | -->
      <!-- <router-link to="/AdClient">AdClient</router-link> | -->
      <router-link to="/Barcode">Barcode</router-link> |
      <router-link to="/ProductDetail">ProductDetail</router-link> |
      <!-- <router-link to="/ProductSizeChart">ProductSizeChart</router-link> |  -->
      <!-- <router-link to="/ProductDetailLocation">ProductDetailLocation</router-link> |  -->
      <router-link to="/ProductSizeRecommand">ProductSizeRecommand</router-link> | 
      <router-link to="/PersonalShopper">PersonalShopper</router-link> | 
      <!-- <span v-if="isLogin"> -->
      <router-link to="/Admin">Admin</router-link> | 
      <router-link to="/ProductForm">ProductForm</router-link> | 
      <router-link to="/ProductUpdateForm">ProductUpdateForm</router-link> | 
      <router-link @click.native="logout" to="#">Logout</router-link> |
      <!-- </span> -->
      <!-- <span v-else> -->
      <router-link :to="{ name: 'Signup' }">Signup</router-link> |
      <router-link :to="{ name: 'Login' }">Login</router-link> |
      <!-- </span> -->
      <!-- <router-view @login="isLogin = true"/> -->
      <router-link to="/Payment">Payment</router-link> | 
      <router-link :to="{ name: 'PersonalShopperDetail' }">PersonalShopperDetail</router-link> |
      <router-link :to="{ name: 'Cart' }">Cart</router-link> |
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  }
}
</script>

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

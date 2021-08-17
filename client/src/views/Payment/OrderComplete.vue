<template>
  <div>
    <Nav/>
    <p>주문이 완료되었습니다 !</p>
    <p>주문 번호는 {{ orderNumber }}입니다.</p>
    <p>{{ $route.params.responseData }}</p>
    <b-button @click="goToMain()" variant="primary">메인으로</b-button>
  </div>
</template>

<script>
import Nav from '../Nav/Nav.vue'

export default {
  components: { Nav },
  name: 'OrderComplete',
  data: function () {
    return {
      orderNumber: Number,
    }
  },
  methods: {
    goToMain () {
      this.$store.dispatch('cart/clearCart')
      this.$router.push('/')
    },
  },
  mounted: function () {
    this.orderNumber = localStorage.getItem('orderNumber')
    setTimeout(() => {
      this.goToMain()
    }, 10000)
  },
}
</script>

<style>

</style>
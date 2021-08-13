<template>
  <div>
    <Nav/>
    <p>주문이 완료되었습니다 !</p>
    <p>주문 번호는 {{ orderNumber }}입니다.</p>
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
      this.$router.push('/')
    },
  },
  mounted: function () {
    if (!localStorage.getItem('orderNumber')) {
      localStorage.setItem('orderNumber', 0)
      this.orderNumber = 0
    } else {
      this.orderNumber = Number(localStorage.getItem('orderNumber')) + 1
      localStorage.setItem('orderNumber', this.orderNumber)  
    }
  },
}
</script>

<style>

</style>
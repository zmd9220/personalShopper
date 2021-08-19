<template>
<!-- Sara로고 -->
  <img src="@/assets/logo.png" alt="logo" class="logo" @click="gotoMain()">
</template>

<script>
export default {
  name: 'Nav',
  methods: {
    gotoMain() {
      this.$router.push('/'); // 메인화면으로 이동
    }
  },

}
</script>

<style>
.logo {
  display: flex;
  width: 30%;
}
</style>
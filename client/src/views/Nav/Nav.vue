<template>
  <img src="@/assets/logo.png" alt="logo" class="logo" @click="gotoMain()">
</template>

<script>
export default {
  name: 'Nav',
  methods: {
    gotoMain() {
      this.$router.push('/');
    }
  },

}
</script>

<style>
.logo {
  display: flex;
  width: 200px;
}
</style>
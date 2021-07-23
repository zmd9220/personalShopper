<template>
  <div id="search-bar">
    <input  type="text" v-model="query" @keyup.enter="onEnter">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data: function () {
    return {
      query: '',
    }
  },
  methods: {
    onEnter: function () {
      this.$emit('search', this.query)
    }
  } 
}
</script>

<style>
#search-bar > input {
  width: 100%;      /* 가로 너비 배치를 화면의 끝과 끝으로 배치 */
  padding: 0.5rem;  /* input 안쪽의 margin을 여유롭게 */
  font-size: 2rem;
}
</style>
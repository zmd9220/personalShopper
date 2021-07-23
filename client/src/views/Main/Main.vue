<template>
  <div>
    <img alt="zara logo" src="https://cdn.iconscout.com/icon/free/png-512/zara-3215529-2673947.png">
    <HelloWorld/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    HelloWorld
  }
}
</script>

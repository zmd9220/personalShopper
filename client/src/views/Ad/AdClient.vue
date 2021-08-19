<template>
  <div>
    <Nav/>
  <div>
    <video class="iframe" autoplay muted ="true" loop="true" >
      <source src="@/assets/ad/y2mate.com - Adidas Orignals Superpower  1st vertical mobile ad commercial_1080p.mp4">
    </video>
  </div>
  </div>
</template>

<script>

import Nav from '@/views/Nav/Nav'


export default {
  name: 'AdClient',
  components: {
    Nav,
  },
  mounted: { // 이용자 부재 시 local 데이터 삭제
    removeData: function() { 
      localStorage.clear()
    }
  }
}
</script>

<style>
section {
  display: flex;
  
}

.iframe {
position: fixed;
right: 0;
bottom: 0;
min-width: 100%;
min-height: 100%;
width: auto;
height: auto;
z-index: -100;
background-size: cover;
}
</style>

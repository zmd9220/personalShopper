<template>
  <div>
    <section>
      <VideoDetail :selectedVideo="selectedVideo"/>
    </section>
      <!-- 자동재생, 전체화면을 위한 iframe -->
      <iframe
        id="ytplayer"
        src="https://www.youtube.com/embed/gKCmezkfWbE?autoplay=1&loop=1&playlist=gKCmezkfWbE"
        type="text/html"
        frameborder="0"
        width="640" height="360" allowfullscreen  allow=autoplay>
      </iframe>
  </div>
</template>

<script>
export default {
  props: {
    selectedVideoURL : { // 추천 1,2,3
      type: String,
    },
  }
}
</script>

<style>
section {
  display: flex;
  
}

iframe {
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
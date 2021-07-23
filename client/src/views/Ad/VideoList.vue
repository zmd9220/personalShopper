<template>
  <ul id="video-list">
    <VideoListItem v-for="video in videoList" 
    :key="video.etag"
    :video="video"
    @select-video="onSelectedVideo"
    />
  </ul>
</template>

<script>
import VideoListItem from '@/views/Ad/VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videoList: {
      type: Array,
      required: true,
    },
  },
  methods: {
    onSelectedVideo: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>
#video-list {
  /* 기본 margin, padding, 그리고 list-style 속성 초기화 */
  padding: 0;
  margin: 0;
  list-style-type: none;
  width: 30%; /* Detail, List의 7:3 가로비율 설정*/
}
</style>
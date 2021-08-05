<template>
  <div >
    <header>
      <SearchBar @search="onSearch"/>
    </header>

    <section>
      <VideoDetail :selectedVideo="selectedVideo" @selectedVideoURL="passVideoURL"/>
      <VideoList :videoList="videoList" @select-video="onSelectedVideo"/>
    </section>
    <AdClient :selectedVideoURL="selectedVideoURL"/>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/views/Ad/SearchBar'
import VideoList from '@/views/Ad/VideoList'
import VideoDetail from '@/views/Ad/VideoDetail'
import AdClient from '@/views/Ad/AdClient'

export default {
  name: 'Ad',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
    AdClient,
  },
  data: function () {
    return {
      videoList: [],
      selectedVideo: null,
      selectedVideoURL: '',
    }
  },
  methods: {
    onSearch: function (query) {
      this.query = query
      const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
      const API_URL = 'https://www.googleapis.com/youtube/v3/search'

      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: query,
      }

      axios({
        method: 'GET',
        url: API_URL,
        params,
      }).then(response => {
        this.videoList = response.data.items
      }).catch(error => {
        console.log(error)
      })
    },
    onSelectedVideo: function (video) {
      this.selectedVideo = video
    },
    passVideoURL: function(selectedVideoURL) {
      this.selectedVideoURL = selectedVideoURL
      console.log(this.selectedVideoURL)
    },
  }
}
</script>

<style>
header {
  width: 80%;
  margin: 0 auto;
  padding: 1rem 0;
}

section {
  display: flex;
  
}
</style>

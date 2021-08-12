<template>
  <div>
    <h4>PersonalShopper</h4>
    <div>{{this.$store.state.user}}</div>
    <b-icon icon="chevron-compact-left" scale="10" variant="dark"></b-icon>
    <img class="product-detail-img" src="@/assets/dummydata/1001.png" alt="personal1" style="width:50%"> 
    <b-icon icon="chevron-compact-right" scale="10" variant="dark"></b-icon>
    <video autoplay >
      <source src="@/assets/ad/y2mate.com - ZARA WOMAN  Spring Summer 2021 Campaign_1080p.mp4">
    </video>


    <div>
      
      
    </div>
    <h4>Look 완성하기</h4>
    <FooterAd/>
  </div>
</template>

<script>
import FooterAd from '@/views/FooterAd/FooterAd'
import { mapState } from 'vuex'

export default {
  components: {
    FooterAd,
  },
  computed: {
    videoElement () {
      return this.$refs.video;
    }, 
    ...mapState(['user'])
  }
}
</script>

<style>

</style>
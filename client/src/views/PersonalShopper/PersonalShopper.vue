<template>
  <div>
    <h4>PersonalShopper</h4>
    <b-icon icon="chevron-compact-left" scale="10" variant="dark"></b-icon>
    <img class="product-detail-img" src="@/assets/dummydata/1001.png" alt="personal1" style="width:50%"> 
    <b-icon icon="chevron-compact-right" scale="10" variant="dark"></b-icon>
    <div>
      
    </div>
    <h4>Look 완성하기</h4>
    <FooterAd/>
  </div>
</template>

<script>
import FooterAd from '@/views/FooterAd/FooterAd'

export default {
  components: {
    FooterAd,
  },
}
</script>

<style>

</style>
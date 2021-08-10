<template>
  <div>
    <Nav/>
    <div class="blank-box"></div>
    <h4>상품의 바코드를</h4>
    <h4>인식기에 보여주세요</h4>
    <div class="blank-box"></div>
    <h4>PersonalShopper의 추천</h4>
    <FooterAd/>
  </div>
</template>

<script>
import FooterAd from '@/views/FooterAd/FooterAd'
import Nav from '@/views/Nav/Nav'
import axios from 'axios'

export default {
  name: 'Barcode',
  components: {
    FooterAd,
    Nav,
  },
  mounted() {
    const postURL = 'http://127.0.0.1:8000/makeStatus/'
    axios.get(postURL)
      .then((res) => {
        console.log(res.status)
      })
  },
}
</script>

<style scoped>
.blank-box {
  height: 15rem;
}
</style>
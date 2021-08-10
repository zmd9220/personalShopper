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
    // 바코드 페이지 렌더링이 끝나고 나서, makeStatus를 통해 서버에 barcode.txt 파일을 생성하도록 요청하고
    // 해당 파일이 생성되면 임베디드 python 코드에서 인식해서 barcode_scan 함수를 실행시킴
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
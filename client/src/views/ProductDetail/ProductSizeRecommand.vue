<template>
  <div>
    <Nav/>
    <!-- 상품이름 연동필요 -->
    <h1 class="text-box-title">스트럭처 셔츠</h1>
    <div class="ProductBox container">
      <img class="ProductDetailImg" src="@/assets/item1.png" alt="item1" style="width:45%">
      <div class="TextBox">       
      </div>
      <div class="slider">
        <label for="range-1" class="question-text">어떤 핏을 원하세요?</label>
        <b-form-input class="silder-bar" id="range-1" v-model="value" type="range" min="0" max="2"></b-form-input>
        <div v-if="this.value === '0'">
          <div class="size-text-container">
            <span class="select-text">타이트하게</span>
            <span>딱 맞게</span>
            <span>헐렁하게</span>
          </div>
        </div>
        <div v-if="this.value === '1'">
          <div class="size-text-container">
            <span>타이트하게</span>
            <span class="select-text">딱 맞게</span>
            <span>헐렁하게</span>
          </div>
        </div>
        <div v-if="this.value === '2'">
          <div class="size-text-container">
            <span>타이트하게</span>
            <span>딱 맞게</span>
            <span class="select-text">헐렁하게</span>
          </div>
        </div>
        <div class="mt-2 selected-size" v-if="this.value === '0'">S (KR 90)</div>
        <div class="mt-2 selected-size" v-if="this.value === '1'">M (KR 95-100)</div>
        <div class="mt-2 selected-size" v-if="this.value === '2'">L (KR 100-105)</div>
      </div>

    </div>

    <h4>PersonalShopper의 추천</h4>
    <FooterAd/>
  </div>
</template>

<script>
import FooterAd from '@/views/FooterAd/FooterAd'
import Nav from '@/views/Nav/Nav'


export default {
  name: 'ProductSizeRecommand',
  components: {
    FooterAd,
    Nav,
  },

  data() {
    return {
      value: '2'
    }
  },
}
</script>

<style scoped>
.ProductBox {
  display: flex;
  margin-bottom: 5rem;
}

.text-box-title {
  font-weight: bold;
  margin-bottom: 3rem;
}

.ProductDetailImg {
  margin-right: 5rem;
}

.TextBox {
  text-align: center;
}

.slider {
  width: 100%;
}

.question-text {
  font-size: 3vh;
}

.silder-bar {
  margin-top: 1rem;
}

.size-text-container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 2rem;
}

.size-text-container .select-text {
  font-weight: bold;
}

.selected-size {
  font-weight: bold;
  font-size: 2rem;
}
</style>






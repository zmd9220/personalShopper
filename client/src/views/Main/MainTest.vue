<template>
  <div class="container">
    <div class="main-column">
      <img src="@/assets/logo.png" alt="logo" class="main-logo">
      <div class="button-text">
        <div>
          <button class="button button-main" button @click="goToBarcode()">
            <img class="img-Barcode" alt="Barcode" src="https://www.pngkey.com/png/full/11-115159_barcode-no-digits-barcode-transparent.png" />
          </button>
        </div>
          바코드로 상품 찾기
      </div>
      <!-- 유저 정보 출력 테스트 -->
      <p>나이, 성별 출력 테스트</p>
      <p>나이 - {{ age }}, 성별 - {{ gen }}</p>
      <div class="button-text">
        <div>
          <button class="button button-main" button @click="goToPersonalShopper()">Personal<br />Shopper</button>
        </div>
        상품 추천 서비스
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MainTest',
  // age - 나이, gen - 성별
  props: {
    age: String,
    gen: String,
  },
  components: {
  },
  methods:{
    goToBarcode(){
      this.$router.push('/Barcode'); 
    },
    goToPersonalShopper(){
      this.$router.push('/PersonalShopper'); 
    }
  },
}
</script>

<style scoped>

.main-column {
  display: flex;
  flex-direction: column;
}

.button {
  border: none;
  border-radius: 20px;
}

.button-main {
  background-color: #e7e7e7;
  font-size: 18px;
  height: 90px;
  width: 240px;
}

.button-text {
  margin-bottom: 90px;
}

.img-Barcode {
  height: 20px;
  width: 90px;
}

.main-logo {
  display: flex;
  width: 600px;
  align-self: center;
}
</style>
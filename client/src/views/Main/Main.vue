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
          <h2 class="button-under-text">바코드로 상품 찾기</h2>
      </div>
      
      <div class="button-text">
        <div>
          <button class="button button-main" button @click="goToPersonalShopper()">Personal<br />Shopper</button>
        </div>
        <h2 class="button-under-text">상품 추천 서비스</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Main',
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

.main-logo {
  width: 200% !important;
}

.button {
  border: none;
  border-radius: 10%;
}

.button-main {
  background-color: #e7e7e7;
  font-size: 5rem;
  height: 25rem;
  width: 100%;
}

.button-text {
  margin-bottom: 90px;
}

.img-Barcode {
  height: 30%;
  width: 50%;
}

.button-under-text {
  font-size: 5rem;
}

.main-logo {
  display: flex;
  width: 20rem;
  align-self: center;
}
</style>
<template>
  <div class="container">
    <div class="row">
      <img alt="zara logo" src="https://cdn.iconscout.com/icon/free/png-512/zara-3215529-2673947.png">
      <div class="button-text">
        <div>
          <button class="button button-main" button @click="goToBarcode()">
            <img class="img-Barcode" alt="Barcode" src="https://www.pngkey.com/png/full/11-115159_barcode-no-digits-barcode-transparent.png" />
          </button>
        </div>
          바코드로 상품 찾기
      </div>
      
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
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
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

</style>
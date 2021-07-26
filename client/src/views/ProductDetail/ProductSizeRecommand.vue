<template>
  <div>
    <Nav/>
    <div class=""> <h1>상품이름</h1></div>
    <div class="ProductBox container">
      <img class="ProductDetailImg" src="@/assets/item1.png" alt="item1" style="width:45%">
      <div class="TextBox">
        

      </div>
    </div>
  

  <div>
    <label for="range-1">Example range with min and max</label>
    <b-form-input id="range-1" v-model="value" type="range" min="0" max="5"></b-form-input>
    <div class="mt-2">Value: {{ value }}</div>
  </div>

    
    <h4>PersonalShopper의 추천</h4>
    <FooterAd/>
  </div>
</template>

<script>
import FooterAd from '@/views/FooterAd/FooterAd'
import Nav from '@/views/Nav/Nav'


export default {
  name: 'Barcode',
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

<style>
.ProductBox {
  display: flex;
  margin-bottom: 5rem;
}

.ProductDetailImg {
  margin-right: 5rem;
}

.TextBox {
  text-align: center;
}

</style>






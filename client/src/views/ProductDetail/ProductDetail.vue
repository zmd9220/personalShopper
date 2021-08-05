<template>
  <div>
    <Nav/>
    <div class="product-box container" :key="productId">
        <img class="product-detail-img" :src=" productDetail.product_image " alt="item1" style="width:45%">
      <div class="text-box">
        <!-- 상품이름 연동필요 -->
        <h2 class="text-box-title">{{ productDetail.product_name }}</h2> 
        <h2>재고정보</h2>
        <div class="size-box">

          <!-- 남자 상의 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'M' && `${productDetail.product_type }` == 1">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <!-- 삼항연산자 stock(재고)유무에 따라 css속성을 바꾼다. 있으면 앞, 없으면 뒤 -->
              <div>
                <span style="text-align: start" >{{manTopSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>
        
          <!-- 남자 하의 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'M' && `${productDetail.product_type }` == 2">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{manBottomSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>                  

          <!-- 여자 상의 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'F' && `${productDetail.product_type }` == 1">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{womanTopSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>        

          <!-- 여자 하의 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'F' && `${productDetail.product_type }` == 2">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{womanBottomSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>

          <!-- 남자 신발 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'M' && `${productDetail.product_type }` == 3">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{manShoesSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>        

          <!-- 여자 신발 -->
          <ul class="size-stock" v-if="`${productDetail.gender }` == 'F' && `${productDetail.product_type }` == 3">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{womanShoesSize[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>                  

          <!-- 악세서리 -->
          <ul class="size-stock" v-if="`${productDetail.product_type }` == 4">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>
                <span style="text-align: start" >{{accessory[i]}}</span>
                <span v-if="stock == 0" class="coming-soon"> Coming soon</span>
              </div>
            </li>
          </ul>          
  
        </div>
        <h2 @click="goToSizeRecommend()">사이즈 추천받기</h2>
        <h2 @click="goToSizeChart()">사이즈표</h2>
        <h2 @click="goToLocation()">상품위치 정보</h2>
      </div>
    </div>
    <h4>PersonalShopper의 추천</h4>
    <FooterAd :productRecommend1="productRecommend1" :productRecommend2="productRecommend2" :productRecommend3="productRecommend3" @selectedProductId="changeProductId"/>
  </div>
</template>

<script>
import FooterAd from '@/views/FooterAd/FooterAd'
import Nav from '@/views/Nav/Nav'
import axios from 'axios'


export default {
  name: 'ProductDetail',
  components: {
    FooterAd,
    Nav,
  },
  data: function() {
    return {
      productDetail: '',
      productImage: '',
      stocks: '',
      productRecommend1: '',    // 리팩토링 필요 (slice => split, props 넘겨주는걸 Array), 추천 1, 2, 3 항목에 해당.
      productRecommend2: '',
      productRecommend3: '',
      manTopSize: ['XS (KR 90)', 'S (KR 95)', 'M (KR 95-100)', 'L (KR 100-105)', 'XL (KR 105-110)'], // 사이즈별 데이터
      womanTopSize: ['XS (KR 44)', 'S (KR 55)', 'M (KR 66)', 'L (KR 77)', 'XL (KR 88)'],
      manBottomSize: ['XS (KR 28)', 'S (KR 30)', 'M (KR 31)', 'L (KR 32)', 'XL (KR 34)'],
      womanBottomSize: ['XS (KR 24)', 'S (KR 26)', 'M (KR 28)', 'L (KR 30)', 'XL (KR 32)'],
      manShoesSize: ['KR 250', 'KR 260', 'KR 270', 'KR 280','KR 290'],
      womanShoesSize: ['KR 230', 'KR 240', 'KR 250', 'KR 260','KR 270'],
      accessory: ['freesize'],
      productId : '101',

      // isActive: False,
    }
  },
  methods :{
    goToSizeRecommend(){
      this.$router.push('/ProductSizeRecommand'); 
    },
    goToSizeChart(){
      this.$router.push('/ProductSizeChart'); 
    },
    goToLocation(){
      this.$router.push('/ProductDetailLocation'); 
    },
    getProduct: function() { // 상품정보를 받아오는 axios
      const localURL = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL = localURL + this.productId + '/'; //
      
      axios.get(productURL) // 리팩토링 필요.
        .then((res) => {
          // console.log(res.data)
          this.productDetail = res.data;
          // this.productImage = require("@/assets/dummydata/" + res.data.product_image)
          this.productRecommend1 = 'http://127.0.0.1:8000/product/' + res.data.style_products.slice(0,3) + '/';
          this.productRecommend2 = res.data.style_products.slice(5,8)
          this.productRecommend3 = res.data.style_products.slice(10,14)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getStock: function() { // 재고정보를 받아오는 axios
      const localURL = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const stockURL = localURL + this.productId + '/' + 'stocks' +'/';
      axios.get(stockURL)
        .then((res) => {
          this.stocks = res.data.stock;       // stock모델은 size가 필요없다. 바꿔야한다.
        })
        .catch((err) => {
          console.log(err)
        })
    },
    changeProductId: function(selectedProductId) {
      console.log(selectedProductId)
      this.productId = selectedProductId;
      this.getProduct();
      this.getStock();
    }
  },
  created: function () { // created로 선언하여 데이터를 갱신한다.
    this.getProduct();
    this.getStock();
  },
  updated: function() {
    // this.productId = selectedProductId
    // this.getProduct();
    // this.getStock();
  }
}

</script>


<style scoped>
.product-box {
  display: flex;
  margin-bottom: 5rem;
}

.product-detail-img {
  margin-right: 5rem;
}

.text-box {
  text-align: center;
}

.size-box {
  display: inline-block;
  width: 100%;
  height: 40%;
  /* background: rgba(66, 60, 60, 0.781); */
}

.size-stock {
  list-style:none;
  padding-left:0px;
  font-size: 2rem;
}

.size-stock li {
  display: flexbox;
}

.size-stock .coming-soon {
  display: flex;
  align-self: end ;
}

.text-box h2 {
  margin: 2rem 0;
}

.text-box .text-box-title {
  margin: 0;
  font-weight: bold;
  font-size: 3rem;
}
</style>
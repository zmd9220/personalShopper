<template>
  <div>
    <Nav/>
    <div class="product-box container">
        <img class="product-detail-img" :src="`${productImage}`" alt="item1" style="width:45%">
      <div class="text-box">
        <!-- 상품이름 연동필요 -->
        <h2 class="text-box-title">{{ productDetail.product_name }}</h2> 
        <h2>재고정보</h2>
        <div class="size-box">


          <ul class="size-stock" v-if="`${productDetail.gender }` == 'M' && `${productDetail.product_type }` == 1">

            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">{{man_upper_size[i]}} : {{stock}}</li>
          </ul>

            <!-- 남자 상의 -->
            <!-- <li v-for="size, idx in man_upper_size" :key="idx">{{size[i]}}</li> -->
          <!-- <ul class="size-stock" v-if="`${productDetail.gender }` == 'M' && `${productDetail.product_type }` == 1">
            <li :style="[stock== 0 ? {color:'rgba(66, 60, 60, 0.4)'} : {color:'#000000'}]" v-for="stock, i in stocks" :key="i">
              <div>

                <span style="text-align: start" >{{man_upper_size[i]}}</span>
                <span v-if="stock == 0" class="comming-soon"> Comming soon</span>
              </div>
            </li>
          </ul> -->
        
        
          <!-- 남자 하의 -->
          <ul v-if="`${productDetail.gender }` == 'M' && `${productDetail.product_type }` == 2">
            <li v-for="stock, i in stocks" :key="i">{{stock}}</li>
          </ul>
                  
        
          <!-- 여자 상의 -->
          <ul v-if="`${productDetail.gender }` == 'F' && `${productDetail.product_type }` == 1">
            <li v-for="stock, i in stocks" :key="i">{{stock}}</li>
          </ul>
        
        
          <!-- 여자 하의 -->
          <ul v-if="`${productDetail.gender }` == 'F' && `${productDetail.product_type }` == 2">
            <li v-for="stock, i in stocks" :key="i">{{stock}}</li>
          </ul>
        
        
          <!-- 남자 신발 -->
          <ul v-if="`${productDetail.gender }` == 'M' && `${productDetail.product_type }` == 3">
            <li v-for="stock, i in stocks" :key="i">{{stock}}</li>
          </ul>
        
        
          <!-- 여자 신발 -->
          <ul v-if="`${productDetail.gender }` == 'F' && `${productDetail.product_type }` == 3">
            <li v-for="stock, i in stocks" :key="i">{{stock}}</li>
          </ul>
                  
        
          <!-- 악세서리 -->
          <ul v-if="`${productDetail.product_type }` == 4">
            <li v-for="stock, i in stocks" :key="i">{{stock}}</li>
          </ul>
          
  
        </div>
        <h2 @click="goToSizeRecommend()">사이즈 추천받기</h2>
        <h2 @click="goToSizeChart()">사이즈표</h2>
        <h2 @click="goToLocation()">상품위치 정보</h2>
      </div>
    </div>
    <h4>PersonalShopper의 추천</h4>
    <FooterAd :style_products = "productDetail.style_products"/>
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
      man_upper_size: ['XS (KR 90)', 'S (KR 95)', 'M (KR 95-100)', 'L (KR 100-105)', 'XL (KR 105-110)'],
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
    getProduct: function() {
      axios.get('http://127.0.0.1:8000/product/301/')
        .then((res) => {
          console.log(res);
          this.productDetail = res.data;
          this.productImage = require("@/assets/dummydata/" + res.data.product_image)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getStock: function() {
      axios.get('http://127.0.0.1:8000/product/301/stocks/')
        .then((res) => {
          console.log(res);
          this.stocks = res.data.stock;       // stock모델은 size가 필요없다. 바꿔야한다.
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () {
    this.getProduct()
    this.getStock()
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

.size-stock .comming-soon {
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
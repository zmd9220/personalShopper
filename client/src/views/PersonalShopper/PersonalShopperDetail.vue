<template>
  <div>
    <Nav/>
    <p class="title">"Look" 4 U</p>  
    <div class="image-area">
      <b-icon class="img-switch-prev" icon="arrow-left-circle-fill" aria-hidden="true"></b-icon>
      <img :src="this.$store.state.productDetail.style_image" alt="look1" class="look-detail">
      <b-icon class="img-switch-next" icon="arrow-right-circle-fill" aria-hidden="true"></b-icon>
    </div>
    <div class="look-items-area">
      <p>룩 완성하기</p>
      <div>
        <p>
          <b-button class="add-items-cart" variant="primary"
            @click="BuyAllItems()">
            <span class="button-text">룩 세트로 구매 <b-icon icon="credit-card" aria-hidden="true"></b-icon></span></b-button>
        </p>
      </div>
      <br>
      <div class="class=look-items">
        <img class="look-item" :src="this.$store.state.productDetail.product_image" alt="item1" @click="gotoDetail1()" >
        <img class="look-item" :src="this.imgUrl1" alt="item2" @click="gotoDetail2()" >
        <img class="look-item" :src="this.imgUrl2" alt="item3" @click="gotoDetail3()" >
        <img class="look-item" :src="this.imgUrl3" alt="item4" @click="gotoDetail4()" >
      </div>
    </div>
    <!-- <FooterAd/> -->
  </div>
</template>

<script>
import Nav from '@/views/Nav/Nav'
import {mapState} from 'vuex';
import axios from 'axios'

export default {
  name: 'PersonalShopperDetail',
  components : {
    Nav,
  },
  data: function() {
    return {
      imgUrl1: '',
      imgUrl2: '',
      imgUrl3: '',
    }
  },
  computed: {
  ...mapState ({
    selectedProductID: state => state.selectedProductID,
    productId_1: state => state.productId_1,
    productId_2: state => state.productId_2,
    productId_3: state => state.productId_3,
    }
  ),
  },
  methods: {
    addToCart: function(product_id) { // 상품정보를 받아오는 axios
      const localURL = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL = localURL + product_id + '/'; //
      
      axios.get(productURL) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.$store.dispatch('cart/addItem', res.data);
        })
        .catch(() => {
          // console.log(err)
        })
    },
    getImageUrl: function() {
      const localURL = 'http://127.0.0.1:8000/product/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      const productURL1 = localURL + this.$store.state.productId_1 + '/'; // 
      const productURL2 = localURL + this.$store.state.productId_2 + '/'; //
      const productURL3 = localURL + this.$store.state.productId_3 + '/'; //
      
      axios.get(productURL1) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.imgUrl1 = res.data.product_image
        })
        .catch(() => {
          // console.log(err)
        })
      axios.get(productURL2) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.imgUrl2 = res.data.product_image
        })
        .catch(() => {
          // console.log(err)
        })
      axios.get(productURL3) // 리팩토링 필요. (async await로 변경예정)
        .then((res) => {
          this.imgUrl3 = res.data.product_image
        })
        .catch(() => {
          // console.log(err)
        })
    },
    BuyAllItems(){
      this.$store.dispatch('cart/addItem', this.$store.state.productDetail);
      this.addToCart(this.$store.state.productId_1);
      this.addToCart(this.$store.state.productId_2);
      this.addToCart(this.$store.state.productId_3);
      this.$router.push({name:'Cart'});
    },
  },
  created: function() {
    this.getImageUrl(this.$store.state.productId_1)
    this.getImageUrl(this.$store.state.productId_2)
    this.getImageUrl(this.$store.state.productId_3)
    this.getImageUrl()
  },
}
</script>

<style>
.title {
  font-size: 4em;
  font-weight: bold;
}

.img-switch-prev {
  margin: 0 2em 0 0;
  font-size: 5.5em;
}

.img-switch-next {
  margin: 0 0 0 2em;
  font-size: 5.5em;
}

.look-detail {
  width: 60%;
}

.add-items-cart {
  width: 25%;
  position: fixed;
  right: 10%;
}

.button-text {
  font-size: 3.25em;
}

.look-items-area {
  position: fixed;
  bottom: 0%;
  font-size: 4em;
  font-weight: bold;
}

.look-item {
  display: inline;
  float: left;
  width: 25%;
  /* margin: 0 0 0 0.2em; */
}
</style>
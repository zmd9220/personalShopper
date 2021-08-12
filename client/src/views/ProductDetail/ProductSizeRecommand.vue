<template>
  <div>
    <Nav/>
    <!-- 상품이름 연동필요 -->
    <h1 class="text-box-title">{{ productDetail.product_name }}</h1>
    <div class="ProductBox container">
      <img class="ProductDetailImg" :src=" productDetail.product_image " alt="item1" style="width:45%">
      <div class="TextBox">       
      </div>

      <div class="slider">
      <div class="modal-info-box">
        <div>
          <b-button v-b-modal.modal-center>Launch centered modal</b-button>

          <b-modal id="modal-center" size="xl" centered title="알맞은 정보를 선택해주세요" >
            <div style="height:5vh">
            </div>
            <h3>키</h3>
            <div class="modal-button">
              <b-button-group size="lg">
                <b-button class="button-option" pill @click="height_change(0)">~{{ this.manHeight }}cm</b-button>
                <b-button class="button-option" pill @click="height_change(1)">{{ this.manHeight }}~{{ this.manHeight+5 }}cm</b-button>
                <b-button class="button-option" pill @click="height_change(2)">{{ this.manHeight+5 }}~{{ this.manHeight+10 }}cm</b-button>
                <b-button class="button-option" pill @click="height_change(3)">{{ this.manHeight+10 }}~{{ this.manHeight+15 }}cm</b-button>
                <b-button class="button-option" pill @click="height_change(4)">{{ this.manHeight+15 }}cm~</b-button>
              </b-button-group>
            </div>
            <div style="height:3vh"></div>
            <h3>몸무게</h3>
            <div class="modal-button">
              <b-button-group size="lg">
                <b-button class="button-option2" @click="weight_change(0)">~{{ this.manWeight }}kg</b-button>
                <b-button class="button-option2" @click="weight_change(1)">{{ this.manWeight }}~{{ this.manWeight+10 }}kg</b-button>
                <b-button class="button-option2" @click="weight_change(2)">{{ this.manWeight+10 }}~{{ this.manWeight+20 }}kg</b-button>
                <b-button class="button-option2" @click="weight_change(3)">{{ this.manWeight+20 }}~{{ this.manWeight+30 }}kg</b-button>
                <b-button class="button-option2" @click="weight_change(4)">{{ this.manWeight+30 }}kg~</b-button>
              </b-button-group>
            </div>
          </b-modal>
        </div>
      </div>
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
        <div class="mt-2 selected-size" v-if="this.value === '0'">{{ this.sizeconvert[this.sizeconvertNum -1] }}</div>
        <div class="mt-2 selected-size" v-if="this.value === '1'">{{ this.sizeconvert[this.sizeconvertNum] }}</div>
        <div class="mt-2 selected-size" v-if="this.value === '2'">{{ this.sizeconvert[this.sizeconvertNum +1] }}</div>
      </div>

    </div>

    <h4>PersonalShopper의 추천</h4>
    <FooterAd  :productRecommend1="productRecommend1" :productRecommend2="productRecommend2" :productRecommend3="productRecommend3" :productId1="productId1" :productId2="productId2" :productId3="productId3" @selectedProductId="changeProductId"/>
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
  props: {
    productRecommend_1 : { // 추천 1,2,3
      type: String,
    },
    productRecommend_2 : {
      type: String,
    },
    productRecommend_3 : {
      type: String,
    },
    productId_1 : { // 추천 ID 1,2,3
      type: Number,
    }, 
    productId_2 : {
      type: Number,
    }, 
    productId_3 : {
      type: Number,
    }, 
    productDetail : {
      type: Object,
    },
  },
  data() {
    return {
      value: '0',
      height: 0,
      weight: 0,
      sizetable : [[1,2,3,4,5],[2,3,3,4,5],[3,4,4,5,6],[2,3,4,5,6],[3,3,4,5,6]],
      sizeconvert : '',
      sizeconvertNum : 1,
      selectedSize: '',
      productRecommend1: this.productRecommend_1,
      productRecommend2: this.productRecommend_2,
      productRecommend3: this.productRecommend_3,
      productId1: this.productId_1,
      productId2: this.productId_2,
      productId3: this.productId_3,
      manWeight: 50,
      manHeight: 165,
      PassProductId: '',
    }
  },
  methods : {
    height_change(num){
      this.height = num
      this.sizeconvertNum = this.sizetable[this.height][this.weight]
    },
    weight_change(num){
      this.weight = num
      this.sizeconvertNum = this.sizetable[this.height][this.weight]
    },
    changeProductId(payload) { // 연관 상품 조회시 그 상품 조회 페이지로 이동.
      this.PassProductId = payload
      console.log(this.PassProductId)
      // this.PassProductId = selectedProductId;
      this.$router.push({
        name:'ProductDetail', 
        params: {
      //     // console.log()
          passProductID: this.PassProductId,
      //     // productRecommend_2: this.productRecommend2,
      //     // productRecommend_3: this.productRecommend3,
      //     // productId_1: this.productId1,
      //     // productId_2: this.productId2,
      //     // productId_3: this.productId3,
      //     // productDetail: this.productDetail,
        }});
      // this.$emit('selectedProductId', selectedProductId);
      // this.getProduct();
      // this.getStock();
    }
  },
  mounted : function(){
    if (this.productDetail.gender != 'M'){
      this.manWeight = this.manWeight -10
      this.manHeight = this.manHeight -15
    }
    if (this.productDetail.gender == 'M' && this.productDetail.product_type == 1){
      this.sizeconvert = ["XS (KR 90)","S (KR 95)","S (KR 95)","M (KR 95-100)","L (KR 100-105)","XL (KR 110-115)","XL (KR 110-115)","XL (KR 110-115)"]
    }
    else if (this.productDetail.gender == 'M' && this.productDetail.product_type == 2){
      this.sizeconvert = ["XS (KR 28)","S (KR 30)","S (KR 30)","M (KR 31)","L (KR 32)","XL (KR 34)","XL (KR 34)","XL (KR 34)"]
    }
    else if (this.productDetail.gender == 'F' && this.productDetail.product_type == 1){
      this.sizeconvert = ["XS (KR 44)","S (KR 55)","S (KR 55)","M (KR 66)","M (KR 66)","L (KR 77)","XL (KR 88)","XL (KR 88)"]
    } else {
      this.sizeconvert = ["XS (KR 24)","S (KR 26)","S (KR 26)","M (KR 28)","L (KR 30)","L (KR 30)","XL (KR 32)","XL (KR 32)"]
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

.modal-info-box {
  width: 100%;
  /* height: 20vh; */
}

.modal-button {
  display: flex;
  justify-content: center;

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

.button-option {
  margin-right: 2rem;
}

.button-option2 {
  border-color: rgb(255, 255, 255);
  border-width: 0.2rem;
}
</style>






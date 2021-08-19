<template>
  <div>
    <Nav/>
    <!-- 상품정보 -->
    <p class="text-box-title">{{ productDetail.product_name }}</p>
    <div class="ProductBox">
      <img class="ProductDetailImg" :src=" productDetail.product_image " alt="item1">

      <div class="slider">
        <label for="range-1" class="question-text">어떤 핏을 원하세요?</label>
        <div class="modal-info-box">
          <div>
            <!-- 키, 몸무게 입력할수있는 버튼 -->
            <b-button v-b-modal.modal-center variant="info" class="size-modal-button">내 정보 입력하기</b-button>
            <b-modal id="modal-center" size="xl" centered title="알맞은 정보를 선택해주세요">
              <template #modal-header>
                <div class="mx-auto size-header">
                  <p>알맞은 정보를 선택해주세요</p>
                </div>
              </template>
              <div style="height:1.5vh"></div>  
              <div class="height-area">
                <p>키 정보를 입력해주세요</p>
                <br>
                <!-- 키 버튼 -->
                <div class="modal-button">
                  <b-button-group>
                    <b-button class="button-option" @click="height_change(0)">~{{ this.manHeight }}cm</b-button>
                    <b-button class="button-option" @click="height_change(1)">{{ this.manHeight }}~{{ this.manHeight+5 }}cm</b-button>
                    <b-button class="button-option" @click="height_change(2)">{{ this.manHeight+5 }}~{{ this.manHeight+10 }}cm</b-button>
                    <b-button class="button-option" @click="height_change(3)">{{ this.manHeight+10 }}~{{ this.manHeight+15 }}cm</b-button>
                    <b-button class="button-option" @click="height_change(4)">{{ this.manHeight+15 }}cm~</b-button>
                  </b-button-group>
                </div>
              </div>
              <div style="height:3vh"></div>
              <div class="weight-area">
                <p>몸무게 정보를 입력해주세요</p>
                <br>
                <!-- 몸무게 버튼 -->
                <div class="modal-button">
                  <b-button-group>
                    <b-button class="button-option" @click="weight_change(0)">~{{ this.manWeight }}kg</b-button>
                    <b-button class="button-option" @click="weight_change(1)">{{ this.manWeight }}~{{ this.manWeight+10 }}kg</b-button>
                    <b-button class="button-option" @click="weight_change(2)">{{ this.manWeight+10 }}~{{ this.manWeight+20 }}kg</b-button>
                    <b-button class="button-option" @click="weight_change(3)">{{ this.manWeight+20 }}~{{ this.manWeight+30 }}kg</b-button>
                    <b-button class="button-option" @click="weight_change(4)">{{ this.manWeight+30 }}kg~</b-button>
                  </b-button-group>
                </div>
              </div>
            </b-modal>
          </div>
        </div>
        <!-- 옷입는 스타일 슬라이드바 -->
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
        <!-- 슬라이드에 선택된 값에따라 추천 사이즈 변경 -->
        <div class="mt-2 selected-size" v-if="this.value === '0'">{{ this.sizeconvert[this.sizeconvertNum -1] }}</div>
        <div class="mt-2 selected-size" v-if="this.value === '1'">{{ this.sizeconvert[this.sizeconvertNum] }}</div>
        <div class="mt-2 selected-size" v-if="this.value === '2'">{{ this.sizeconvert[this.sizeconvertNum +1] }}</div>
      </div>

    </div>
    <div class="footer-row">
      <p>PersonalShopper의 추천</p>
      <br>
      <FooterAd :productRecommend1="productRecommend1" :productRecommend2="productRecommend2" :productRecommend3="productRecommend3" :productId1="productId1" :productId2="productId2" :productId3="productId3" @selectedProductId="changeProductId"/>
    </div>
  </div>
</template>

<script>
import FooterAd from '@/views/FooterAd/FooterAd'
import Nav from '@/views/Nav/Nav'
import {mapState} from 'vuex'

export default {
  name: 'ProductSizeRecommand',
  components: {
    FooterAd,
    Nav,
  },
  computed: {
    ...mapState({
      selectedProductID: state => state.selectedProductID, // 메인상품
      productDetail: state => state.productDetail, // 메인상품 상세정보
      productLocation: state => state.productLocation, // 메인상품 위치
      productRecommend_1:  state => state.productRecommend_1, // 추천아이템들
      productRecommend_2:  state => state.productRecommend_2,
      productRecommend_3:  state => state.productRecommend_3,
      productId_1:  state => state.productId_1,
      productId_2:  state => state.productId_2,
      productId_3:  state => state.productId_3,
      stock: state => state.stock, // 메인상품 재고정보
    })
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
      productRecommend1: this.$store.state.productRecommend_1,
      productRecommend2: this.$store.state.productRecommend_2,
      productRecommend3: this.$store.state.productRecommend_3,
      productId1: this.$store.state.productId_1,
      productId2: this.$store.state.productId_2,
      productId3: this.$store.state.productId_3,
      manWeight: 50, // 기본 남자 몸무게
      manHeight: 165, // 기본 남자 키
      PassProductId: '',
      productDetail: this.$store.state.productDetail,
    }
  },
  methods : {
    height_change(num){ // 키 변경 함수
      this.height = num
      this.sizeconvertNum = this.sizetable[this.height][this.weight]
    },
    weight_change(num){ // 몸무게 변경 함수
      this.weight = num
      this.sizeconvertNum = this.sizetable[this.height][this.weight]
    },
    changeProductId(payload) { // 연관 상품 조회시 그 상품 조회 페이지로 이동.
      this.PassProductId = payload
      console.log(this.PassProductId)
      this.$router.push({
        name:'ProductDetail', 
        params: {
          passProductID: this.PassProductId,
        }});
    }
  },
  mounted : function(){
    if (this.productDetail.gender != 'M'){ // 성별과 제품타입에 따른 사이즈 표기 변경 함수
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
  margin-bottom: 5em;
  position: fixed;
  left: 5%;
  width: 90%;
  font-size: 0.25em;
}

.text-box-title {
  font-weight: bold;
  margin-bottom: 3em;
  font-size: 2em;
}

.ProductDetailImg {
  margin-right: 5em;
  width: 50%;
}

.TextBox {
  text-align: center;
}

.size-header {
  font-size: 1.5em;
}

.modal-info-box {
  width: 100%;
}

.size-modal-button {
  width: 60%;
  font-size: 3em;
}

.modal-button {
  display: flex;
  justify-content: center;
  width: 100%;
}

.slider {
  display: flex;
  flex-direction: column;
  align-self:center;
  width: 100%;
}

.height-area {
  text-align: center;
  font-size: 1em;
}

.weight-area {
  text-align: center;
  font-size: 1em;
}

.question-text {
  font-size: 5em;
  margin-bottom: 1em;
}

.silder-bar {
  margin-top: 5em;
  margin-bottom: 2em;
}

.size-text-container {
  display: flex;
  justify-content: space-between;
  margin-bottom: 3em;
  font-size: 2.5em;
}

.size-text-container .select-text {
  font-weight: bold;
}

.selected-size {
  font-weight: bold;
  font-size: 5em;
}

.button-option {
  border-color: rgb(255, 255, 255);
  border-width: 0.2em;
  width: 7.5em;
  font-size: 0.75em;
}

.footer-row {
  position: fixed;
  bottom: 0%;
}
</style>






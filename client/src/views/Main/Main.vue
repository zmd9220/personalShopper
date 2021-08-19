<template>
  <div class="container">
    <div class="main-column">
      <!-- 로고 -->
      <img src="@/assets/logo.png" alt="logo" class="main-logo" />
      <div class="button-text">
        <div>
          <!-- 바코드버튼 -->
          <button
            class="button button-main"
            button
            @click="recommendDataBarcode()" 
          >
            <img
              class="img-Barcode"
              alt="Barcode"
              src="https://www.pngkey.com/png/full/11-115159_barcode-no-digits-barcode-transparent.png"
            />
          </button>
        </div>
        바코드로 상품 찾기
      </div>
      <!-- 퍼스널쇼퍼 버튼 -->
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
import { mapState } from "vuex";
import axios from "axios";

export default {
  name: "Main",
  // url에서 나이 성별 데이터 가져오기
  // age - 나이, gen - 성별
  props: {
    age: String,
    gen: String,
  },
  data: function () {
    return {
      userData: [{ age: this.age }, { gen: this.gen }], // 사용자 나이, 성별 담기는 변수
      recomendData: [], // 추천 알고리즘 통해서 받아오는 상품 ID 값들 담기는 변수
    };
  },
  computed: {
    ...mapState ({
      selectedProductID: state => state.selectedProductID, // vuex 활용하여 첫번째 상품 ID 담기
      productId_1: state => state.productId_1, // vuex 활용하여 두번째 상품 ID 담기
      productId_2: state => state.productId_2, // vuex 활용하여 세번째 상품 ID 담기
      productId_3: state => state.productId_3, // vuex 활용하여 네번째 상품 ID 담기
      } 
    ),
    },
  methods:{
    goToBarcode(){ // 바코드페이지로 이동하는 함수
      this.$router.push('/Barcode'); 
    },
    goToPersonalShopper() { // PersonalShopper페이지로 이동하는 함수
      this.$router.push("/PersonalShopper");
    },
    createUserData: function () { // 사용자 정보 vuex로 담는 함수
      this.$store.dispatch("createUserData", {age: this.age , gen: this.gen})
      localStorage.setItem('user', JSON.stringify({age: this.age , gen: this.gen}))
    },
    recommendData() { // django로 사용자 정보 보내서 django 내부에 추천알고리즘 통하여 추천상품 ID 값들 요청하는 함수
      const localURL = "http://127.0.0.1:8000/recommended/";
      const fm = new FormData();
      fm.append("age", this.age);
      fm.append("gen", this.gen);

      axios
        .post(localURL, fm)
        .then((res) => {
          this.$store.commit('selectedProductID', Number(res.data.slice(7,10)));
          this.$store.commit('productId_1', Number(res.data.slice(19,22)));
          this.$store.commit('productId_2', Number(res.data.slice(31,34)));
          this.$store.commit('productId_3', Number(res.data.slice(43,46)));
        })
        .catch((error) => {
          console.log(error);
        })
    },
    recommendDataBarcode() { // django로 사용자 정보 보내서 django 내부에 추천알고리즘 통하여 추천상품 ID 값들 요청하는 함수
      const localURL = "http://127.0.0.1:8000/recommended/";
      const fm = new FormData();
      fm.append("age", this.age);
      fm.append("gen", this.gen);

      axios
        .post(localURL, fm)
        .then((res) => {
          console.log(res);
          localStorage.setItem("recommendData", res.data);
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          this.goToBarcode()
        })

    },
  },
  mounted: function () {
    this.createUserData() // 사용자 정보 vuex로 담는 함수

    },
  created : function() {
    this.recommendData(); // django로 사용자 정보 보내서 django 내부에 추천알고리즘 통하여 추천상품 ID 값들 요청하는 함수
  },
}
</script>

<style scoped>

.main-column {
  display: flex;
  flex-direction: column;
}

.main-logo {
  width: 100%;
  margin-top: 5%;
  margin-bottom: 18rem;
}

.button {
  border: none;
  border-radius: 10%;
}

.button-main {
  background-color: #e7e7e7;
  font-size: 2.5rem;
  height: 10rem;
  width: 40%;
  position: relative;
  border-radius: 0.75em;
  margin-bottom: 2rem ;
}

.button-text {
  margin-bottom: 5rem;
  font-size: 2em;
}

.img-Barcode {
  height: 30%;
  width: 50%;
  position: absolute;  
  top: 0;  
  bottom: 0;  
  left: 0;  
  right: 0;  
  margin: auto;
}

.PS-btn-text {
  margin-bottom: 0;
}

.button-under-text {
  font-size: 30em;
}

.main-logo {
  display: flex;
  width:60em;
  align-self: center;
}
</style>
<template>
  <div class="container">
    <div class="main-column">
      <img src="@/assets/logo.png" alt="logo" class="main-logo" />
      <div class="button-text">
        <div>
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
      <!-- 유저 정보 출력 테스트 -->
      <p>나이, 성별 출력 테스트</p>
      <p>나이 - {{ age }}, 성별 - {{ gen }}</p>
      <div class="button-text">
        <div>
          <!-- <button class="button button-main" button @click="recommendData()">
            Personal<br />Shopper
          </button> -->
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
  name: "MainTest",
  // age - 나이, gen - 성별
  props: {
    age: String,
    gen: String,
  },
  data: function () {
    return {
      userData: [{ age: this.age }, { gen: this.gen }],
      recomendData: [],
    };
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
  methods:{
    goToBarcode(){
      this.$router.push('/Barcode'); 
    },
    goToPersonalShopper() {
      this.$router.push("/PersonalShopper");
    },
    createUserData: function () {
      this.$store.dispatch("createUserData", {age: this.age , gen: this.gen});
    },
    recommendData() {
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
    recommendDataBarcode() {
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
    this.createUserData()

    },
  created : function() {
    this.recommendData();
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
<template>
  <div>
    <div class="footer">
      <div class="footer-text">
        <p>PersonalShopper의 추천</p>
      </div>
      <!-- 추천 아이템들 -->
      <div class="footer-row">
        <div class="column">
          <img
            class="product-detail-img"
            :src="this.productDetail1.product_image"
            alt="personal1"
            style="width: 100%"
            @click="gotoDetail1()"
          />
        </div>

        <div class="column">
          <img
            class="product-detail-img"
            :src="this.productDetail2.product_image"
            alt="personal2"
            style="width: 100%"
            @click="gotoDetail2()" 
          />
        </div>

        <div class="column">
          <img
            class="product-detail-img"
            :src="this.productDetail3.product_image"
            alt="personal3"
            style="width: 100%"
            @click="gotoDetail3()" 
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import axios from "axios";

export default {
  props: {},
  data: function () {
    return {
      productDetail1: "", // 상품정보
      productDetail2: "", // 상품정보
      productDetail3: "", // 상품정보
      recommendProductId: JSON.parse(localStorage.getItem("recommendData")),
    };
  },
  computed: {
    ...mapState({
      selectedProductID: (state) => state.selectedProductID, // 추천 시스템에 활용될 메인 Product
      productRecommend_1: (state) => state.productRecommend_1, // 추천 아이템들.
      productRecommend_2: (state) => state.productRecommend_2,
      productRecommend_3: (state) => state.productRecommend_3,
      productId_1: (state) => state.productId_1,
      productId_2: (state) => state.productId_2,
      productId_3: (state) => state.productId_3,
    }),
  },
  methods: {
    gotoDetail1: function() { // selectedProductID를 변경하고 Detail page로 보내기
        this.$store.commit('selectedProductID', this.productDetail1.product_id);
        this.$router.push({name:'ProductDetail'});
    },
    gotoDetail2: function() { // selectedProductID를 변경하고 Detail page로 보내기
        this.$store.commit('selectedProductID', this.productDetail2.product_id);
        this.$router.push({name:'ProductDetail'});
    },
    gotoDetail3: function() { // selectedProductID를 변경하고 Detail page로 보내기
        this.$store.commit('selectedProductID', this.productDetail3.product_id);
        this.$router.push({name:'ProductDetail'});
    },
    getProduct: function () {
      // 상품정보를 받아오는 axios
      const localURL1 = "http://127.0.0.1:8000/product/"; 
      const productURL1 = localURL1 + this.recommendProductId["A"] + "/"; //

      axios
        .get(productURL1) 
        .then((res) => {
          this.productDetail1 = res.data; // 상품 상세 정보
          this.$store.commit("productDetail1", res.data); // 상품 상세정보
        })
        .catch(() => {
          // console.log(err)
        });

      const localURL2 = "http://127.0.0.1:8000/product/"; 
      const productURL2 = localURL2 + this.recommendProductId["B"] + "/"; //

      axios
        .get(productURL2) 
        .then((res) => {
          this.productDetail2 = res.data; // 상품 상세 정보
          this.$store.commit("productDetail2", res.data); // 상품 상세정보
        })
        .catch(() => {
          // console.log(err)
        });

      const localURL3 = "http://127.0.0.1:8000/product/"; 
      const productURL3 = localURL3 + this.recommendProductId["C"] + "/"; //

      axios
        .get(productURL3) 
        .then((res) => {
          this.productDetail3 = res.data; // 상품 상세 정보
          this.$store.commit("productDetail3", res.data); // 상품 상세정보
        })
        .catch(() => {
          // console.log(err)
        });
    },
  },
  created: function () {
    // created로 선언하여 데이터를 갱신한다.
    this.getProduct(); // 상품정보
  },
};
</script>

<style scoped>
.footer {
  display: contents;
}

.footer-text {
  font-size: 1.5em;
  position: fixed;
  bottom: 30%;
  left: 0%;
  right: 0%;
}

.footer-row {
  display: flex;
  width: 100%;
  position: fixed;
  bottom: 0%;
}

.column {
  display: inline;
  float: left;
  width: 33.3%;
  margin: 0 0.05em;
}
</style>
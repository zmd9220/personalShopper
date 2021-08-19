<template>
  <div>
    <Nav />
    <!-- 바코드 입력 페이지 -->
    <div>
      <div class="blank-box"></div>
      <p class="barcode-text">상품의 바코드를</p>
      <p class="barcode-text">인식기에 보여주세요</p>
      <div class="blank-box"></div>
    </div>
    <!-- 입력받은 고객 연령/성별 데이터에 기반하여 footer에 상품 추천 -->
    <div class="footer-row">
      <br />
      <FooterAdBarcode
        :productRecommend1="productRecommend1"
        :productRecommend2="productRecommend2"
        :productRecommend3="productRecommend3"
        :productId1="productId1"
        :productId2="productId2"
        :productId3="productId3"
        @selectedProductId="changeProductId"
      />
    </div>
  </div>
</template>

<script>
import FooterAdBarcode from "@/views/FooterAd/FooterAdBarcode";
import Nav from "@/views/Nav/Nav";
import axios from "axios";

export default {
  name: "Barcode",
  components: {
    FooterAdBarcode,
    Nav,
  },
  mounted() {
    // 바코드 페이지 렌더링이 끝나고 나서, makeStatus를 통해 서버에 barcode.txt 파일을 생성하도록 요청하고
    // 해당 파일이 생성되면 임베디드 python 코드에서 인식해서 barcode_scan 함수를 실행시킴
    const postURL = "http://127.0.0.1:8000/makeStatus/";
    axios.get(postURL).then((res) => {
      console.log(res.status);
    });
  },
  // 받을 데이터 변수 설정
  data: function () {
    return { 
      productRecommend1: "",
      productRecommend2: "",
      productRecommend3: "",
    };
  },
  methods: {
    // footer에서 상품 선택 시 선택한 상품의 상세 페이지로 이동
    changeProductId(payload) { 
      console.log(payload);
      this.$router.push({
        name: "ProductDetail",
        params: {
          passProductID: payload,
        },
      });
    },
  },
};
</script>

<style scoped>
.blank-box {
  height: 8rem;
}

.barcode-text {
  font-size: 1.5em;
}
</style>
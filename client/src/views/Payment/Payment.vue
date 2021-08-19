<template>
  <div>
    <!-- 결제 버튼 -->
    <b-button @click="kakaoPayReady()" variant="white"><img class="pay-btn" src="@/assets/kakaopay/payment_icon_yellow_large.png" alt="pay button"></b-button>
  </div>
</template>

<script>
import axios from 'axios'
import {mapState, mapGetters} from 'vuex'

export default {
  name: 'Payment',
  props: {
    product: Object,
  },
  methods:{
      kakaoPayReady(){
        // 모든 옷들이 사이즈 선택 완료 되었을 때 코드 실행
        if (this.$store.state.cart.selectSizeCnt === this.$store.state.cart.items.length) {
          // 
          let baseUrl = "http://127.0.0.1:8000/"
          // 로컬 저장소에 주문 번호 데이터가 없을경우 (첫 주문) 로컬에 첫 데이터 넣기
          if (!localStorage.getItem('orderNumber')) {
            localStorage.setItem('orderNumber', 0)
          }
          // 장바구니 데이터 추후 재갱신을 위해 로컬저장소에 저장
          localStorage.setItem('items', JSON.stringify(this.orderItems))
          // 유저 정보 데이터 추후 재갱신을 위해 로컬저장소에 저장
          localStorage.setItem('user', JSON.stringify(this.userData))
          // 요청을 보낼 데이터 생성
          let requestData = {
            product_name: (this.orderItems.length > 1) ? this.orderItems[0].product_name + ' 외 ' + String(this.orderItems.length-1) + '건' : this.orderItems[0].product_name,
            price: this.totalCartPrice,
            orderNumber: 0,
          }
          requestData.orderNumber = Number(localStorage.getItem('orderNumber')) + 1
          axios({
            method: 'POST',
            url: baseUrl + "kakaoPayReady/",
            data: requestData,
          }).then((res) =>{
            // 카카오 페이 페이지 url
            let payUrl = res.data.next_redirect_pc_url
            // 승인시 필요한 tid를 추후에 사용하기 위해 로컬저장소에 저장
            localStorage.setItem('tid', res.data.tid)
            // 카카오 API에서 응답으로 안내한 결제 페이지로 이동
            location.href = payUrl
          })
          // axios에 문제가 발생했을 경우
          .catch((error) =>{
            alert("에러가 발생했습니다. 다시 시도해주세요")
            console.log(error)
          })
          // 사이즈 선택이 다 되지 않았을 경우
        } else {
          alert("사이즈를 선택해주세요.")
        }
      }
  },
  computed: {
    ...mapGetters('cart',{
      totalCartPrice: 'totalPrice',
    }),
    ...mapState('cart',{
      orderItems: 'items',
    }),
    ...mapState({
      userData: 'user',
    }),
  }
}
</script>

<style>

.pay-text {
  margin-top: 0.5em;
  font-size: 1em;
}

.pay-btn {
  width: 75%
}

</style>
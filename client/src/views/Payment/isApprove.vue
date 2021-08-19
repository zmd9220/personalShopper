<template>
  <div>
  </div>
</template>

<script>
import axios from 'axios'
import {mapState} from 'vuex'

export default {
  name: 'isApprove',
  data: function () {
    return {
      paymentData: {
        pg_token: String,
        tid: String,
        orderNumber: Number,
      },
    }
  },
  methods: {
    approve () {
      // axios 요청을 위한 api 서버 url
      let baseUrl = "http://127.0.0.1:8000/"
      // 요청에 담아 보낼 데이터 (기존 결제 데이터 + 유저, 장바구니 내역도 함께)
      let requestData = this.paymentData
      requestData.userData = this.userData
      requestData.orderItems = this.orderItems
      // axios 요청
      axios({
        method: 'POST',
        url: baseUrl + "kakaoPayApprove/",
        data: requestData,
      }).then((res) =>{
        // 요청이 제대로 왔을 때 데이터를 받기
        let responseData = res.data
        // 상태 코드가 200 = 제대로 승인 완료 되었음
        if (responseData.status_code === 200) {
          // 로컬저장소의 주문 번호 완전히 갱신
          localStorage.setItem('orderNumber', Number(localStorage.getItem('orderNumber')) + 1) 
          localStorage.setItem('paymentData', JSON.stringify(responseData))
          // 주문 완료 페이지로 이동 (결제 관련 정보와 함께) 
          this.$router.push({name: 'OrderComplete', params: {responseData: responseData}})
        } else {
          // 결제까지는 문제없이 갔는데, 승인에 문제가 있었을 경우 승인 에러 코드와 메세지 출력
          alert('Error code : ' + responseData.code + '\n' + responseData.extras.method_result_message)
          // 다시 장바구니 페이지로 돌아가도록
          this.$router.push({name: 'Cart'})
        }
      }).catch((error) =>{
        // 서버에서 정상적으로 응답을 받지 못했을 때
        alert("에러가 발생했습니다. 다시 시도해주세요")
        console.log(error)
        // 다시 장바구니 페이지로
        this.$router.push({name: 'Cart'})
      })
    },
    makeData () {
      // 혹시 모를 promise 객체화 하여 비동기로 먼저 끝내도록 구성
      return new Promise( () => {
        // tid, orderNumber 가져오기
        this.paymentData.tid = localStorage.getItem('tid')
        this.paymentData.orderNumber = Number(localStorage.getItem('orderNumber')) + 1
        // 카카오 페이 결제 페이지를 갔다오면 vuex가 초기화 됨. 그래서 로컬 저장소의 저장 내역을 토대로 다시 vuex에 저장
        this.$store.dispatch("createUserData", JSON.parse(localStorage.getItem('user'))) 
        this.$store.dispatch("cart/cartReload", JSON.parse(localStorage.getItem('items')))
      })
    },
  },
  mounted: function () {
    if (this.$route.query.pg_token) {
      // 정상적으로 토큰이 발급된 경우
      // 보낼 데이터에 토큰 담기
      this.paymentData.pg_token = this.$route.query.pg_token
      // localstorage.getItem으로 인해(데이터를 가져오는 속도보다 코드 진행속도가 더 빠름) 비동기 처리가 필요 - 함수화 하여 데이터 저장
      this.makeData()
      // axios 요청을 통해 승인 요청 보내기
      this.approve()
    } else {
      // 정상적으로 토큰이 발급되지 않은 경우 (결제 취소)   
      alert('결제를 취소했습니다.')
      // 장바구니로 돌아가기
      this.$router.push({name: 'Cart'})
    }
  },
  computed: {
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

</style>

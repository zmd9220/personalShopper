<template>
  <div>
    <p>{{ $route.query }}</p>
    <p>{{ paymentData.pg_token }}</p>
    <p>{{ paymentData.tid }} </p>
    <p>{{ paymentData.orderNumber }} </p>
  </div>
</template>

<script>
import axios from 'axios'

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
      let baseUrl = "http://127.0.0.1:8000/"
      console.log(this.paymentData)
      axios({
        method: 'POST',
        url: baseUrl + "kakaoPayApprove/",
        data: this.paymentData,
      }).then((res) =>{
          let payUrl = res.data
          console.log(res)
          console.log(payUrl)
          // location.href = payUrl
          // OpenWin_variety(payUrl,'결제 페이지')
          // window.open(payUrl, '_parent', 'width=800, height=600')
      })
      .catch((error) =>{
          alert("에러가 발생했습니다. 다시 시도해주세요")
          console.log(error)
          // this.$router.push('/')
      })
    },
    makeData () {
      return new Promise( () => {
        let nowTid = localStorage.getItem('tid')
        let nowOrderNumber = localStorage.getItem('orderNumber')
        this.paymentData.tid = nowTid
        this.paymentData.orderNumber = nowOrderNumber
        console.log(this.paymentData.tid)
        console.log(this.paymentData.orderNumber)
      })
    },
  },
  mounted: function () {
    // 정상적으로 토큰이 발급된 경우
    if (this.$route.query.pg_token) {
      console.log(this.$route.query)
      this.paymentData.pg_token = this.$route.query.pg_token
      // this.makeData().then(() => {
      //   console.log('makeData com')
      //   this.approve()
      // })
      this.makeData()
      this.approve()
      // this.makeData()
    // 정상적으로 토큰이 발급되지 않은 경우 (결제 취소)   
    } else {
      alert('결제를 취소했습니다.')
      this.$router.push({name:'Payment', params: {product: localStorage.getItem('orderedProduct')}})
    }
  }
}
</script>

<style>

</style>
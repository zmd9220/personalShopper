<template>
  <div>
    <!-- <p>{{ $route.query }}</p>
    <p>{{ paymentData.pg_token }}</p>
    <p>{{ paymentData.tid }} </p>
    <p>{{ paymentData.orderNumber }} </p> -->
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
      let baseUrl = "http://127.0.0.1:8000/"
      // console.log(this.paymentData)
      let requestData = this.paymentData
      console.log(this.userData)
      console.log(this.orderItems)
      requestData.userData = this.userData
      requestData.orderItems = this.orderItems
      console.log(requestData)
      axios({
        method: 'POST',
        url: baseUrl + "kakaoPayApprove/",
        data: requestData,
      }).then((res) =>{
          let responseData = res.data
          if (responseData.status_code === 200) {
            localStorage.setItem('orderNumber', Number(localStorage.getItem('orderNumber')) + 1)  
            this.$router.push({name: 'OrderComplete', params: {responseData: responseData}})
          } else {
            alert('Error code : ' + responseData.code + '\n' + responseData.extras.method_result_message)
            this.$router.push({name: 'Cart'})
          }
        
      })
      .catch((error) =>{
          alert("에러가 발생했습니다. 다시 시도해주세요")
          console.log(error)
          // this.$router.push('/')
      })
    },
    makeData () {
      return new Promise( () => {
        this.paymentData.tid = localStorage.getItem('tid')
        this.paymentData.orderNumber = Number(localStorage.getItem('orderNumber')) + 1
        this.$store.dispatch("createUserData", JSON.parse(localStorage.getItem('user'))) 
        this.$store.dispatch("cart/cartReload", JSON.parse(localStorage.getItem('items')))
      })
    },
  },
  mounted: function () {
    if (this.$route.query.pg_token) {
      // 정상적으로 토큰이 발급된 경우
      // console.log(this.$route.query)
      this.paymentData.pg_token = this.$route.query.pg_token
      // this.makeData().then(() => {
      //   console.log('makeData com')
      //   this.approve()
      // })
      this.makeData()
      this.approve()
    } else {
      // 정상적으로 토큰이 발급되지 않은 경우 (결제 취소)   
      alert('결제를 취소했습니다.')
      // this.$router.push({name:'Payment', params: {product: localStorage.getItem('orderedProduct')}})
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
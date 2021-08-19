<template>
  <div>
    <span>{{ $route.params.product }}</span>
    <b-button @click="pay2()" variant="white"><img class="pay-btn" src="@/assets/kakaopay/payment_icon_yellow_large.png" alt="pay button"></b-button>
    <b-modal
      v-model="show"
      title="결제하기"
      :value="value"
    >

      <b-container fluid>
        <b-row class="mb-1 text-center">
          <b-col cols="3"></b-col>
          <b-col>결제 정보 입력</b-col>
        </b-row>

        <b-row class="mb-1">
          <b-col cols="3">충전금액</b-col>
          <b-col>
            <b-form-select
              v-model="value"
              :options="items"
            ></b-form-select>
          </b-col>
        </b-row>
      </b-container>

      <template #modal-footer>
        <div class="w-100">
          <b-button
            variant="primary"
            size="sm"
            class="float-right"
            @click="pay"
          >
            결제
          </b-button>
          <b-button
            variant="primary"
            size="sm"
            class="float-right"
            value=''
            @click="show=false"
            
          >
            취소
          </b-button>
        </div>
      </template>
    </b-modal> 
  </div>
</template>

<script>
import axios from 'axios'
import {mapState, mapGetters} from 'vuex'

export default {
  components: {  },
  name: 'Payment',
  props: {
    product: Object,
  },
  data: () => ({
    show: false,
    items: [5000, 10000, 20000],
    value: ''
  }),
  methods:{
      pay(){
          let baseUrl = "http://127.0.0.1:8000/"
          let productData = this.product
          if (!localStorage.getItem('orderNumber')) {
            localStorage.setItem('orderNumber', 0)
          } else {
            localStorage.setItem('orderNumber', Number(localStorage.getItem('orderNumber')) + 1)  
          }          
          productData.orderNumber = Number(localStorage.getItem('orderNumber'))
          axios({
            method: 'POST',
            url: baseUrl + "kakaoPayReady/",
            data: productData,
          }).then((res) =>{
              let payUrl = res.data.next_redirect_pc_url
              localStorage.setItem('tid', res.data.tid)
              localStorage.setItem('orderedProduct', productData)
              console.log(res)
              console.log(payUrl)
              location.href = payUrl
          })
          .catch((error) =>{
              alert("에러가 발생했습니다. 다시 시도해주세요")
              console.log(error)
          })
      },
      pay2(){
        if (this.$store.state.cart.selectSizeCnt === this.$store.state.cart.items.length) {

          let baseUrl = "http://127.0.0.1:8000/"
          if (!localStorage.getItem('orderNumber')) {
            localStorage.setItem('orderNumber', 0)
          }
          localStorage.setItem('items', JSON.stringify(this.orderItems))
          localStorage.setItem('user', JSON.stringify(this.userData))
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
            let payUrl = res.data.next_redirect_pc_url
              localStorage.setItem('tid', res.data.tid)
              console.log(res)
              console.log(payUrl)
              location.href = payUrl
          })
          .catch((error) =>{
            alert("에러가 발생했습니다. 다시 시도해주세요")
              console.log(error)

          })
        } else {
          alert("사이즈를 선택해주세요.")
        }
      }
  },
  mounted: function () {
    console.log(this.orderItems)
    console.log(this.userData)
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
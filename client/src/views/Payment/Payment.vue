<template>
  <div>
    <Nav/>
    <span>{{ $route.params.product }}</span>


    <b-button @click="show=true" variant="wihte"><img src="@/assets/kakaopay/payment_icon_yellow_large.png" alt=""></b-button>
    <b-button @click="pay()" variant="white"><img src="@/assets/kakaopay/payment_icon_yellow_large.png" alt="pay button"></b-button>

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
import Nav from '../Nav/Nav.vue'

export default {
  components: { Nav },
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
          // let form = new FormData()
          // form.append('amount', this.value)
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
              // OpenWin_variety(payUrl,'결제 페이지')
              // window.open(payUrl, '_parent', 'width=800, height=600')
          })
          .catch((error) =>{
              alert("에러가 발생했습니다. 다시 시도해주세요")
              console.log(error)
              // this.$router.push('/')
          })
      }
  }
}
</script>
<template>
  <div>
    <b-button @click="show=true" variant="wihte"><img src="@/assets/kakaopay/payment_icon_yellow_large.png" alt=""></b-button>

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

export default {
    name: 'Payment',
    data: () => ({
      show: false,
      items: [5000, 10000, 20000],
      value: ''
    }),
    methods:{
        pay(){
            let baseUrl = "http://127.0.0.1:8000/"
            let form = new FormData()
            form.append('amount', this.value)
            axios.post(baseUrl+"kakaoPay/", form)
            .then(res =>{
                let payUrl = res.data.next_redirect_pc_url
                console.log(res)
                console.log(payUrl)
                location.href = payUrl
            })
            .catch(error =>{
                alert("에러가 발생했습니다. 다시 시도해주세요")
                console.log(error)
                this.$router.push('/')
            })
        }
    }
}
</script>
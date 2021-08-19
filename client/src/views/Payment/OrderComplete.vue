<template>
  <div>
    <Nav/>
    <!-- 결제 성공, 결제와 관련된 내용 출력 -->
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
            <td align="center">
                <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:1200px;">
                    <tr>
                        <td align="center" style="padding: 35px 35px 20px 35px; background-color: #ffffff;" bgcolor="#ffffff">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:1200px;">
                                <tr>
                                    <td align="center" style="font-family: 'Noto Sans KR', sans-serif; font-size: 16px; font-weight: 500; line-height: 24px; padding-top: 25px;"> <img src="https://img.icons8.com/carbon-copy/100/000000/checked-checkbox.png" width="125" height="120" style="display: block; border: 0px;" /><br>
                                        <h2 style="font-size: 60px; font-weight: 800; line-height: 36px; color: #333333; margin: 0;"> 주문이 완료되었습니다 ! </h2>
                                    </td>
                                </tr>
                                <br>
                                <br>
                                <tr>
                                    <td align="center" style="font-family: 'Noto Sans KR', sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 10px;">
                                        <p style="font-size: 40px; font-weight: 400; line-height: 24px; color: #777777;"> 주문하신 상품은 카운터에 준비되어 있습니다. </p>
                                    </td>
                                </tr>
                                <br>
                                <tr>
                                    <td align="left" style="padding-top: 20px;">
                                        <table cellspacing="0" cellpadding="0" border="0" width="100%">
                                            <tr>
                                                <td width="60%" align="left" bgcolor="#eeeeee" style="font-size: 30px; font-weight: 800; line-height: 50px; padding: 10px;"> 주문 번호 </td>
                                                <td width="40%" align="left" bgcolor="#eeeeee" style="font-size: 30px; font-weight: 800; line-height: 50px; padding: 10px;"> {{ orderNumber }} </td>
                                            </tr>
                                            <tr>
                                                <td width="60%" align="left" style="font-size: 30px; font-weight: 400; line-height: 50px; padding: 15px 10px 5px 10px;"> 주문명 </td>
                                                <td width="40%" align="left" style="font-size: 30px; font-weight: 400; line-height: 50px; padding: 15px 10px 5px 10px;"> {{ paymentData.item_name }} </td>
                                            </tr>
                                            <tr>
                                                <td width="60%" align="left" style="font-size: 30px; font-weight: 400; line-height: 50px; padding: 5px 10px;"> 주문 시간 </td>
                                                <td width="40%" align="left" style="font-size: 30px; font-weight: 400; line-height: 50px; padding: 5px 10px;"> {{ paymentData.approved_at.slice(0, 10) }} {{ paymentData.approved_at.slice(11) }} </td>
                                            </tr>
                                            <tr>
                                                <td width="60%" align="left" style="font-size: 30px; font-weight: 400; line-height: 50px; padding: 5px 10px;"> 결제 타입 </td>
                                                <td width="40%" align="left" style="font-size: 30px; font-weight: 400; line-height: 50px; padding: 5px 10px;"> {{ paymentData.payment_method_type === 'MONEY' ? '카카오페이 현금 결제' : '카카오페이 카드 결제' }} </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="left" style="padding-top: 20px;">
                                        <table cellspacing="0" cellpadding="0" border="0" width="100%">
                                            <tr>
                                                <td width="60%" align="left" style="font-size: 30px; font-weight: 800; line-height: 50px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> 총 결제 금액 </td>
                                                <td width="40%" align="left" style="font-size: 30px; font-weight: 800; line-height: 50px; padding: 10px; border-top: 3px solid #eeeeee; border-bottom: 3px solid #eeeeee;"> {{ $route.params.responseData.amount.total }}원 </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <br>
                    <tr>
                        <td align="center" style=" padding: 35px; background-color: #eeeeee;" bgcolor="#eeeeee">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;">
                                <tr>
                                    <td align="center" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding-top: 25px;">
                                        <h2 style="font-size: 30px; font-weight: 800; line-height: 40px; margin: 0;"> 구매해 주셔서 감사합니다. </h2>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center" style="padding: 25px 0 15px 0;">
                                        <table border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td @click="goToMain()" align="center" style="border-radius: 5px; color: #ffffff; text-decoration: none; background-color: #F44336; padding: 15px 25px; border: 1px solid #F44336; display: block; font-size: 27px;" bgcolor="#66b3b7">메인으로 </td>
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    <br>
                    <tr>
                        <td align="center" style="padding: 35px; background-color: #ffffff;" bgcolor="#ffffff">
                            <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:1200px;">
                                <tr>
                                    <td align="center" style="font-size: 18px; font-weight: 600; line-height: 24px; padding: 5px 0 10px 0;">
                                        <p style="font-size: 35px; font-weight: 600; line-height: 35px; color: #333333; "> 주식회사 SARA </p>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: 400; line-height: 24px;">
                                        <p style="font-size: 30px; font-weight: 400; line-height: 35px; color: #777777;"> If you want contact us, <br> Please send an email to <a href="#" target="_blank" style="color: #777777;">contact.sara.com</a>. </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
  </div>
</template>

<script>
import Nav from '../Nav/Nav.vue'
import {mapState} from 'vuex'

export default {
  components: { Nav },
  name: 'OrderComplete',
  data: function () {
    return {
      orderNumber: Number,
      paymentData: JSON.parse(localStorage.getItem('paymentData')),
    }
  },
  methods: {
    goToMain () {
      // vuex에 장바구니 데이터 삭제
      this.$store.dispatch('cart/clearCart')
      // 로컬저장소 결제 관련 데이터 삭제
      localStorage.removeItem('paymentData')
      // 로컬저장소 장바구니 데이터 삭제
      localStorage.removeItem('items')
      // 메인으로 이동
      this.$router.push('/')
    },
  },
  mounted: function () {
    // 주문 번호 가져오기
    this.orderNumber = localStorage.getItem('orderNumber')
    // 10초 후에 자동으로 함수 실행
    setTimeout(() => {
      this.goToMain()
    }, 10000)
  },
  computed: {
    ...mapState('cart',{
      orderItems: 'items',
    }),
  }
}
</script>

<style>
  body,
  table,
  td,
  a {
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
  }

  table,
  td {
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
      font-family: 'Noto Sans KR', sans-serif;
  }

  img {
      -ms-interpolation-mode: bicubic;
  }

  img {
      border: 0;
      height: auto;
      line-height: 100%;
      outline: none;
      text-decoration: none;
  }

  table {
      border-collapse: collapse !important;
  }

  body {
      height: 100% !important;
      margin: 0 !important;
      padding: 0 !important;
      width: 100% !important;
  }

  a[x-apple-data-detectors] {
      color: inherit !important;
      text-decoration: none !important;
      font-size: inherit !important;
      font-family: inherit !important;
      font-weight: inherit !important;
      line-height: inherit !important;
  }

  @media screen and (max-width: 480px) {
      .mobile-hide {
          display: none !important;
      }

      .mobile-center {
          text-align: center !important;
      }
  }

  div[style*="margin: 16px 0;"] {
      margin: 0 !important;
  }
</style>
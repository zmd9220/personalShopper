<template>
  <div>
    <Nav/>
    <!-- 장바구니 정보 표시 -->
    <div class="table-header">
      <div class="product-name">이름</div>
      <div class="product-size">사이즈</div>
      <div class="product-price">가격</div>
      <div class="product-delete">
        <b-button class="delete-button"
          variant="danger" @click="clearCart()">카트 비우기</b-button>
      </div>
    </div>
    <CartList/>
    <!-- 결제 정보 표시 -->
    <div class="money-box">
      <span class="cart-text">총 금액</span>
      <span class="cart-text">{{ totalCartPrice }} 원</span>
      <Payment/>
    </div>
  </div>
</template>

<script>
import Nav from '@/views/Nav/Nav'
import CartList from '@/views/Cart/CartList.vue'
import Payment from '@/views/Payment/Payment'
import { mapGetters } from 'vuex'

export default {
  name: 'Cart',
  components: {
    Nav,
    CartList,
    Payment,
  },
  methods: {
    clearCart() { //장바구니 비우는 함수
      this.$store.dispatch('cart/clearCart');
    }
  },
  computed: {
    ...mapGetters('cart',{ // 장바구니의 총합을 계산하는 함수
      totalCartPrice: 'totalPrice',
    }),
  }
}
</script>

<style scoped>
.mb-3 {
  width: 80%;
  margin: auto;
  border: 5px solid rgba(0, 0, 0, 0.3);
  border-radius: 5rem;
  font-size: 3rem;
  height: 8rem;
}

.card-img-left {
  border-radius: 5rem 0 0 5rem;
}

.cart-text{
  width: 100%;
}

.table-header {
  display: flex;
  width: 90%;
  margin: auto;
  margin-bottom: 1em;
  border: 2.5px solid rgba(0, 0, 0, 0.3);
  border-radius: 2.5rem;
  font-size: 1.5em;
  align-items: center;
}
.product-name {
  margin-left: 10em;
}
.product-size {
  margin-left: 8rem;
}
.product-price {
  margin-left: 8rem;
}
.product-delete {
  margin-left: 8rem;
}

.delete-button {
  font-size: 0.85em;
  margin-left: 0.9em;
  border-radius: 2.5rem;
}

.money-box {
  width: 15rem;
  height: 15rem;
  border: 2.5px solid rgba(0, 0, 0, 0.3);
  border-radius: 2rem;
  position: fixed;
  bottom: 10%;
  right: 10%;
  align-items: center;
}

.cart-text {
  display: block;
  font-size:2rem;
  padding-top: 0.5em;
}
</style>
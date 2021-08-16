<template>
  <div>
    <Nav/>
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
    <div class="money-box">
      <p class="cart-text">총 금액</p>
      <p class="cart-text">{{ totalCartPrice }} 원</p>
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
    clearCart() {
      this.$store.dispatch('cart/clearCart');
    }
  },
  computed: {
    ...mapGetters('cart',{
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
  width: 1718px;
  margin: auto;
  margin-bottom: 1rem;
  border: 5px solid rgba(0, 0, 0, 0.3);
  border-radius: 5rem;
  font-size: 3rem;
  height: 8rem; 
}
.product-name {
  margin-left: 38rem;
  margin-top: 2rem;
}
.product-size {
  margin-left: 13rem;
  margin-top: 2rem;
}
.product-price {
  margin-left: 7rem;
  margin-top: 2rem;
}
.product-delete {
  margin-left: 8rem;
  margin-top: 1.2rem;
}

.delete-button {
  font-size: 0.85em;
}

.money-box {
  width: 30rem;
  height: 45rem;
  border: 5px solid rgba(0, 0, 0, 0.3);
  border-radius: 5rem;
  margin-left: 95rem;
  margin-top: 6rem;
}

.cart-text {
  font-size: 5rem;
  margin: 4.5rem 0;
}
</style>